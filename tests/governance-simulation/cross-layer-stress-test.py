# SPDX-License-Identifier: Apache-2.0

#!/usr/bin/env python3
"""
Title: AEIP Cross-Layer Governance Simulation Module
Version: 1.0.0
Date: 2025-05-09T00:00:00Z
Author: Repository Architect
License: CC BY-SA 4.0
Signature: Pending governance signature

Simulates cross-layer governance stress tests using AEIP artifact exchanges.
"""

from __future__ import annotations

import json
import statistics
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Sequence

LATENCY_THRESHOLD_MINUTES = 180.0
SCHEMA_DIRECTORY = Path(__file__).resolve().parents[2] / "schemas"
SCHEMA_FILES: Mapping[str, str] = {
    "InterpretiveTracePackage": "interpretive-trace-package.jsonld",
    "DecisionRationaleRecord": "decision-rationale-record.jsonld",
    "GovernanceDecisionSummary": "governance-decision-summary.jsonld",
    "OversightAuditMemo": "oversight-audit-memo.jsonld",
    "IntegrityLedgerEntry": "integrity-ledger-entry.jsonld",
}
DEPENDENCY_RULES: Mapping[str, Sequence[str]] = {
    "DecisionRationaleRecord": ("InterpretiveTracePackage",),
    "GovernanceDecisionSummary": ("DecisionRationaleRecord",),
    "OversightAuditMemo": ("GovernanceDecisionSummary",),
    "IntegrityLedgerEntry": ("GovernanceDecisionSummary", "OversightAuditMemo"),
}
WEIGHTS = {
    "dependency": 0.4,
    "temporal": 0.35,
    "signature": 0.25,
}


@dataclass(frozen=True)
class Artifact:
    """Represents an AEIP artifact exemplar used for simulation."""

    artifact_type: str
    uuid: str
    layer: int
    timestamp: datetime
    linked_artifacts: Sequence[str]
    signature: Mapping[str, str]


@dataclass(frozen=True)
class BaseMetrics:
    """Stores baseline metrics and latency profiles for an artifact."""

    dependency_score: float
    temporal_score: float
    signature_score: float
    mean_latency_minutes: float
    dependencies_expected: int
    dependencies_resolved: int


@dataclass(frozen=True)
class ScenarioMetrics:
    """Captures scenario-adjusted resilience metrics for a layer."""

    dependency_score: float
    temporal_score: float
    signature_score: float
    resilience_index: float


@dataclass(frozen=True)
class ScenarioResult:
    """Groups the descriptive context and metrics for a stress scenario."""

    description: str
    layer_metrics: Mapping[int, ScenarioMetrics]


@dataclass(frozen=True)
class StressScenario:
    """Defines governance stress factors applied to the AEIP exchange chain."""

    name: str
    description: str
    link_degradation: Mapping[str, float]
    latency_offset_minutes: Mapping[str, float]
    signature_compromise: Mapping[str, float]


class CrossLayerGovernanceSimulation:
    """Executes stress-test simulations across AI OSI Stack Layers 4–7."""

    def __init__(self, schema_directory: Path | None = None) -> None:
        self.schema_directory = schema_directory or SCHEMA_DIRECTORY
        self.artifacts: Dict[str, Artifact] = {}
        self.base_metrics: Dict[str, BaseMetrics] = {}

    # ------------------------------------------------------------------
    # Artifact loading
    # ------------------------------------------------------------------
    def load_examples(self) -> None:
        """Loads exemplar artifacts from the JSON-LD schema definitions."""

        artifacts: MutableMapping[str, Artifact] = {}
        for artifact_type, filename in SCHEMA_FILES.items():
            schema_path = self.schema_directory / filename
            with schema_path.open("r", encoding="utf-8") as handle:
                schema = json.load(handle)
            examples = schema.get("examples") or []
            if not examples:
                raise ValueError(
                    f"Schema {filename} does not provide exemplar payloads."
                )
            exemplar = examples[0]
            artifacts[artifact_type] = Artifact(
                artifact_type=artifact_type,
                uuid=exemplar["uuid"],
                layer=int(exemplar["layer"]),
                timestamp=self._parse_timestamp(exemplar["timestamp"]),
                linked_artifacts=tuple(exemplar.get("linked_artifacts", [])),
                signature=dict(exemplar.get("signature", {})),
            )
        self.artifacts = dict(artifacts)

    # ------------------------------------------------------------------
    # Metric computation
    # ------------------------------------------------------------------
    def compute_base_metrics(self) -> None:
        """Computes baseline metrics using exemplar link fidelity and timing."""

        if not self.artifacts:
            self.load_examples()

        metrics: Dict[str, BaseMetrics] = {}
        for artifact_type, artifact in self.artifacts.items():
            dependencies = self._resolve_dependencies(artifact)
            expected = len(DEPENDENCY_RULES.get(artifact_type, ()))
            resolved = len(dependencies)
            dependency_score = 1.0 if expected == 0 else resolved / expected
            latency_minutes = self._compute_latency_minutes(artifact, dependencies)
            temporal_score = self._temporal_score(latency_minutes)
            signature_score = self._signature_score(artifact.signature)
            metrics[artifact_type] = BaseMetrics(
                dependency_score=dependency_score,
                temporal_score=temporal_score,
                signature_score=signature_score,
                mean_latency_minutes=latency_minutes,
                dependencies_expected=expected,
                dependencies_resolved=resolved,
            )
        self.base_metrics = metrics

    # ------------------------------------------------------------------
    # Simulation execution
    # ------------------------------------------------------------------
    def run(self, scenarios: Iterable[StressScenario]) -> Dict[str, ScenarioResult]:
        """Evaluates resilience metrics for Layers 4–7 under stress scenarios."""

        if not self.base_metrics:
            self.compute_base_metrics()

        results: Dict[str, ScenarioResult] = {}
        for scenario in scenarios:
            layer_results: Dict[int, ScenarioMetrics] = {}
            for artifact_type, artifact in self.artifacts.items():
                if artifact.layer < 4 or artifact.layer > 7:
                    continue
                base = self.base_metrics[artifact_type]
                dependency_score = self._apply_degradation(
                    base.dependency_score,
                    scenario.link_degradation.get(artifact_type, 0.0),
                )
                latency_offset = scenario.latency_offset_minutes.get(artifact_type, 0.0)
                temporal_score = self._temporal_score(
                    base.mean_latency_minutes + latency_offset
                )
                signature_score = self._apply_degradation(
                    base.signature_score,
                    scenario.signature_compromise.get(artifact_type, 0.0),
                )
                resilience_index = self._resilience_index(
                    dependency_score, temporal_score, signature_score
                )
                layer_results[artifact.layer] = ScenarioMetrics(
                    dependency_score=dependency_score,
                    temporal_score=temporal_score,
                    signature_score=signature_score,
                    resilience_index=resilience_index,
                )
            results[scenario.name] = ScenarioResult(
                description=scenario.description,
                layer_metrics=dict(layer_results),
            )
        return results

    def render(self, simulation_results: Mapping[str, ScenarioResult]) -> None:
        """Renders scenario metrics using a governance-formatted table."""

        for scenario_name, result in simulation_results.items():
            print(f"Scenario: {scenario_name}")
            print("Description: " + result.description)
            print(
                "Layer | Artifact Type | Dependency | Temporal | Signature | Resilience"
            )
            print(
                "------|----------------|-----------|----------|-----------|-----------"
            )
            for layer in sorted(result.layer_metrics):
                artifact = self._artifact_by_layer(layer)
                metrics = result.layer_metrics[layer]
                print(
                    f"L{layer}   | {artifact.artifact_type:16} | "
                    f"{metrics.dependency_score:0.3f}      | "
                    f"{metrics.temporal_score:0.3f}    | "
                    f"{metrics.signature_score:0.3f}     | "
                    f"{metrics.resilience_index:0.3f}"
                )
            print()

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _artifact_by_layer(self, layer: int) -> Artifact:
        for artifact in self.artifacts.values():
            if artifact.layer == layer:
                return artifact
        raise KeyError(f"No artifact exemplar found for Layer {layer}.")

    def _parse_timestamp(self, value: str) -> datetime:
        iso_value = value.replace("Z", "+00:00") if value.endswith("Z") else value
        timestamp = datetime.fromisoformat(iso_value)
        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=timezone.utc)
        return timestamp.astimezone(timezone.utc)

    def _resolve_dependencies(self, artifact: Artifact) -> List[Artifact]:
        expected_types = DEPENDENCY_RULES.get(artifact.artifact_type, ())
        resolved: List[Artifact] = []
        for expected_type in expected_types:
            dependency = self.artifacts.get(expected_type)
            if dependency and dependency.uuid in artifact.linked_artifacts:
                resolved.append(dependency)
        return resolved

    def _compute_latency_minutes(
        self, artifact: Artifact, dependencies: Sequence[Artifact]
    ) -> float:
        if not dependencies:
            return 0.0
        deltas = [
            abs((artifact.timestamp - dependency.timestamp).total_seconds()) / 60.0
            for dependency in dependencies
        ]
        return float(statistics.mean(deltas))

    def _temporal_score(self, mean_latency_minutes: float) -> float:
        normalized = max(0.0, 1.0 - (mean_latency_minutes / LATENCY_THRESHOLD_MINUTES))
        return round(normalized, 3)

    def _signature_score(self, signature: Mapping[str, str]) -> float:
        required_fields = ("method", "key_id", "value")
        completeness = all(signature.get(field) for field in required_fields)
        return 1.0 if completeness else 0.0

    def _apply_degradation(self, baseline: float, degradation: float) -> float:
        adjusted = baseline * (1.0 - max(0.0, min(degradation, 1.0)))
        return round(max(0.0, adjusted), 3)

    def _resilience_index(
        self, dependency: float, temporal: float, signature: float
    ) -> float:
        score = (
            dependency * WEIGHTS["dependency"]
            + temporal * WEIGHTS["temporal"]
            + signature * WEIGHTS["signature"]
        )
        return round(score, 3)


DEFAULT_SCENARIOS: Sequence[StressScenario] = (
    StressScenario(
        name="interpretability-delay",
        description=(
            "Layer 3 interpretability refresh delays reduce the immediacy of deliberation and "
            "operational translation activities across Layers 4–5."
        ),
        link_degradation={
            "DecisionRationaleRecord": 0.15,
            "GovernanceDecisionSummary": 0.1,
        },
        latency_offset_minutes={
            "DecisionRationaleRecord": 45.0,
            "GovernanceDecisionSummary": 30.0,
        },
        signature_compromise={},
    ),
    StressScenario(
        name="oversight-surge",
        description=(
            "Concurrent assurance demands strain Layer 6 audit throughput, delaying oversight memo "
            "issuance and ledger notarization."
        ),
        link_degradation={
            "OversightAuditMemo": 0.25,
            "IntegrityLedgerEntry": 0.2,
        },
        latency_offset_minutes={
            "OversightAuditMemo": 90.0,
            "IntegrityLedgerEntry": 60.0,
        },
        signature_compromise={
            "OversightAuditMemo": 0.1,
        },
    ),
    StressScenario(
        name="ledger-rekey",
        description=(
            "Cryptographic rekeying temporarily constrains Layer 7 ledger operations and requires "
            "additional validation rounds for connected artifacts."
        ),
        link_degradation={
            "IntegrityLedgerEntry": 0.1,
        },
        latency_offset_minutes={
            "IntegrityLedgerEntry": 30.0,
        },
        signature_compromise={
            "IntegrityLedgerEntry": 0.3,
        },
    ),
)


def main() -> None:
    simulation = CrossLayerGovernanceSimulation()
    simulation.load_examples()
    simulation.compute_base_metrics()
    results = simulation.run(DEFAULT_SCENARIOS)
    simulation.render(results)


if __name__ == "__main__":
    main()
