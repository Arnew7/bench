from dataclasses import dataclass
from statistics import mean
from typing import Optional, List

@dataclass
class SingleResult:
    status: Optional[int]
    elapsed_ms: float
    error: Optional[str]

@dataclass
class HostReport:
    host: str
    success: int
    failed: int
    errors: int
    times_ms: List[float]

    @property
    def min_ms(self) -> Optional[float]:
        return min(self.times_ms) if self.times_ms else None

    @property
    def max_ms(self) -> Optional[float]:
        return max(self.times_ms) if self.times_ms else None

    @property
    def avg_ms(self) -> Optional[float]:
        return mean(self.times_ms) if self.times_ms else None
