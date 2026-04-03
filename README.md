# Autonomous Self-Healing Multi-Agent Firewall

This repository contains the codebase for the EB-2 NIW research project: **"Autonomous Self-Healing Multi-Agent Firewalls: Zero-Touch Immunization in Production LLM Systems"**.

## Architecture Overview
This project demonstrates a multi-agent orchestration setup featuring a **Worker Agent** and an autonomous **Security Agent**.
When the worker agent is successfully compromised via prompt injection, the orchestrator's execution log is audited by the Security Agent. The Security Agent intelligently identifies the vulnerability and permanently patches the worker agent's system boundaries in real-time by dynamically rewriting its system prompt (`src/prompts.json`).

## How to Run the Demo

1. Clone or open the repository.
2. Provide your Anthropic API Key inside the `.env` file!
3. Run the complete autonomous demonstration:
   ```bash
   PYTHONPATH=. python src/demo_self_healing.py
   ```

### 3-Stage Execution Flow:
- **STAGE 1**: The system is instantiated in a vulnerable state. A User executes an attack payload to read the `.env` file. The Coder agent succeeds in exfiltrating the secrets.
- **STAGE 2**: The Security Agent audits the execution log, realizes the Coder leaked secrets, and rewrites the physical `prompts.json` on the disk to immunize the system.
- **STAGE 3**: We simulate the attacker attempting the exact same payload again. The Coder agent, picking up its "Healed" system constraints, permanently blocks the request.
