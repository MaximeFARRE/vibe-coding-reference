"""Données du rapport, conformes aux champs des schémas V0.1."""
from dataclasses import dataclass, field


@dataclass
class Evidence:
    kind: str
    summary: str
    path: str | None = None
    line_start: int | None = None
    command: str | None = None
    exit_code: int | None = None
    redacted: bool | None = None


@dataclass
class Finding:
    id: str
    title: str
    category: str
    severity: str
    status: str
    confidence: str
    origin: str
    summary: str
    evidence: list[Evidence] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)


@dataclass
class CheckResult:
    id: str
    status: str
    reason: str


@dataclass
class Run:
    schema_version: str
    run_id: str
    created_at: str
    workflow: str
    target: dict
    profile: list[str]
    checks: list[CheckResult]
    limitations: list[str]
    findings: list[Finding]
