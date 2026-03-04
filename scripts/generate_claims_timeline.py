from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse


DOMAIN_MAP: Dict[str, str] = {
    "acquisition.gov": "Acquisition.gov",
    "anthropic.com": "Anthropic",
    "apnews.com": "AP News",
    "archives.gov": "NARA",
    "arstechnica.com": "Ars Technica",
    "armscontrol.org": "Arms Control Assoc",
    "autonomousweapons.org": "Autonomous Weapons Org",
    "axios.com": "Axios",
    "bbc.com": "BBC",
    "bloomberg.com": "Bloomberg",
    "businesstoday.in": "Business Today",
    "cbsnews.com": "CBS News",
    "cnbc.com": "CNBC",
    "cnn.com": "CNN",
    "congress.gov": "Congress",
    "csis.org": "CSIS",
    "csmonitor.com": "Christian Science Monitor",
    "csoonline.com": "CSO Online",
    "defensescoop.com": "DefenseScoop",
    "defense.gov": "DoD",
    "engadget.com": "Engadget",
    "eff.org": "EFF",
    "federalregister.gov": "Federal Register",
    "fortune.com": "Fortune",
    "gao.gov": "GAO",
    "govinfo.gov": "GovInfo",
    "justsecurity.org": "Just Security",
    "lawfaremedia.org": "Lawfare",
    "lawfareblog.com": "Lawfare",
    "lawfareblog.org": "Lawfare",
    "law.com": "Law.com",
    "loc.gov": "LOC",
    "media.defense.gov": "DoD",
    "nbcnews.com": "NBC News",
    "newsweek.com": "Newsweek",
    "npr.org": "NPR",
    "nytimes.com": "NYT",
    "openai.com": "OpenAI",
    "politico.com": "Politico",
    "press.un.org": "UN",
    "reuters.com": "Reuters",
    "rstreet.org": "R Street",
    "supremecourt.gov": "Supreme Court",
    "techcrunch.com": "TechCrunch",
    "thehill.com": "The Hill",
    "theverge.com": "The Verge",
    "tile.loc.gov": "LOC",
    "trendsresearch.org": "Trends Research",
    "un.org": "UN",
    "vox.com": "Vox",
    "wapo.st": "Washington Post",
    "washingtonpost.com": "Washington Post",
    "warontherocks.com": "War on the Rocks",
    "wsj.com": "WSJ",
    "yalelawandpolicy.org": "Yale Law & Policy Review",
}

SUBDOMAIN_FILTER = {"www", "www2", "m", "amp"}


def truncate(text: str, limit: int = 100) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def parse_date_str(raw: str) -> Optional[date]:
    if not raw or raw.strip().upper() == "N/A":
        return None

    patterns = [
        (r"(\d{4})-(\d{2})-(\d{2})", "ymd"),
        (r"(\d{4})-(\d{2})", "ym"),
        (r"(\d{4})", "y"),
    ]

    for pattern, kind in patterns:
        match = re.search(pattern, raw)
        if not match:
            continue
        try:
            year = int(match.group(1))
            if kind == "ymd":
                month = int(match.group(2))
                day = int(match.group(3))
            elif kind == "ym":
                month = int(match.group(2))
                day = 1
            else:
                month = 1
                day = 1
            if not 1 <= month <= 12:
                continue
            if not 1 <= day <= 31:
                continue
            return date(year, month, day)
        except ValueError:
            continue
    return None


def extract_first_url(cell: str) -> Optional[str]:
    if not cell or cell.strip().upper() == "N/A":
        return None
    link_match = re.search(r"\((https?://[^)]+)\)", cell)
    if link_match:
        return link_match.group(1).strip()
    loose_match = re.search(r"(https?://\S+)", cell)
    if loose_match:
        return loose_match.group(1).strip().rstrip(")")
    return None


def publication_from_url(url: Optional[str]) -> str:
    if not url:
        return "N/A"

    parsed = urlparse(url)
    netloc = parsed.netloc.lower()
    netloc = netloc.split("@")[-1].split(":")[0]

    if netloc in DOMAIN_MAP:
        return DOMAIN_MAP[netloc]

    # Normalize subdomains.
    parts = [part for part in netloc.split(".") if part and part not in SUBDOMAIN_FILTER]
    if not parts:
        return netloc or "N/A"

    # Handle country-code style domains like co.uk.
    if (
        len(parts) >= 3
        and parts[-1] in {"uk", "au", "in", "ca", "us"}
        and parts[-2] in {"co", "com", "org", "gov", "ac", "edu", "net"}
    ):
        core = parts[-3]
    else:
        core = parts[-2] if len(parts) >= 2 else parts[0]

    core = core.replace("-", " ")
    if core.isupper() or (core.isalpha() and len(core) <= 4):
        return core.upper()
    return core.title()


def parse_claims_table(lines: List[str]) -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    in_table = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|----"):
            in_table = True
            continue
        if not in_table or not stripped.startswith("|"):
            continue

        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 9:
            continue

        claim_id = cells[0]
        if not claim_id or not claim_id.startswith("C"):
            continue

        claim_text = cells[1]
        event_date_text = cells[3]
        reporting_date_text = cells[4]
        primary_links = cells[5]
        secondary_links = cells[6]

        primary_url = extract_first_url(primary_links)
        secondary_url = extract_first_url(secondary_links)
        source_url = primary_url or secondary_url

        rows.append(
            {
                "id": claim_id,
                "event_date": event_date_text,
                "reporting_date": reporting_date_text,
                "claim": claim_text,
                "source_publication": publication_from_url(source_url),
                "event_date_parsed": parse_date_str(event_date_text),
                "reporting_date_parsed": parse_date_str(reporting_date_text),
            }
        )
    return rows


def build_table(rows: List[Dict[str, str]]) -> str:
    header = [
        "# Claims Timeline (Chronological)",
        "",
        "| ID | Event Date | Reporting Date | Claim | Source Publication |",
        "|----|------------|----------------|-------|--------------------|",
    ]
    body = []
    for row in rows:
        body.append(
            f"| {row['id']} | {row['event_date']} | {row['reporting_date']} | "
            f"{truncate(row['claim'])} | {row['source_publication']} |"
        )
    return "\n".join(header + body) + "\n"


def sort_rows(rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
    far_future = date.max
    return sorted(
        rows,
        key=lambda r: (
            r["event_date_parsed"] or far_future,
            r["reporting_date_parsed"] or far_future,
            r["id"],
        ),
    )


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    claims_path = repo_root / "claims.md"
    output_path = repo_root / "docs" / "claims-timeline-chronological.md"

    lines = claims_path.read_text(encoding="utf-8").splitlines()
    parsed_rows = parse_claims_table(lines)
    sorted_rows = sort_rows(parsed_rows)
    output_markdown = build_table(sorted_rows)
    output_path.write_text(output_markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
