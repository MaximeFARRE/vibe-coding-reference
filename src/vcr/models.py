"""Données du rapport, conformes aux champs des schémas V0.1."""
from dataclasses import dataclass, field


@dataclass
class Evidence:
    kind: str
    summary: str
    path: str | None = None
    line_start: int | None = None
    line_end: int | None = None
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
    impact: str = ''
    alternatives: list[str] = field(default_factory=list)
    risks_of_fix: list[str] = field(default_factory=list)
    invariants_to_preserve: list[str] = field(default_factory=list)
    verification_plan: list[str] = field(default_factory=list)
    limitations: list[str] = field(default_factory=list)
    rule_id: str | None = None
    cause: str | None = None


@dataclass
class CheckResult:
    id: str
    status: str
    reason: str
    evidence: list[Evidence] | None = None
    source_method: str | None = None
    applicability_reason: str | None = None
    limitation: str | None = None


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


@dataclass
class ImprovementProposal:
    id: str
    scope: str
    title: str
    sources: list[dict]
    suspected_cause: str
    solution_a: str
    solution_b: str
    risk: str
    maintenance: str
    approval_status: str
    updated_at: str
    reevaluate_when: str
