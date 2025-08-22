from typing import List
from .models import HostReport

def format_report(reports: List[HostReport]) -> str:
    lines = []
    for rep in reports:
        lines.append("="*72)
        lines.append(f"Host   : {rep.host}")
        lines.append(f"Success: {rep.success}")
        lines.append(f"Failed : {rep.failed}")
        lines.append(f"Errors : {rep.errors}")
        if rep.times_ms:
            lines.append(f"Min    : {rep.min_ms:.2f} ms")
            lines.append(f"Max    : {rep.max_ms:.2f} ms")
            lines.append(f"Avg    : {rep.avg_ms:.2f} ms")
        else:
            lines.append("Min    : n/a")
            lines.append("Max    : n/a")
            lines.append("Avg    : n/a")
    lines.append("="*72)
    return "\n".join(lines)
