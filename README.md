# Cerberus v0.3: Hybrid 5G/Mesh Communication System Simulation

This repository contains the complete conceptual codebase for Cerberus v0.3, a sophisticated, multi-modal communication system designed for drone swarms. The system architecture is built around a hybrid 5G and mesh networking model, with additional capabilities for satellite and emergency beacon communications.

**Note:** This is a Python-based **simulation** of the Cerberus v0.3 architecture. It uses mock objects and simulated environments to demonstrate the core logic, security features, and decision-making processes of the system. It is not a deployable, hardware-integrated application.

## Architectural Overview

The Cerberus v0.3 architecture is highly modular, with a clear separation of concerns to ensure resilience and adaptability. Key components include:

*   **Communication Manager**: The central "brain" of the system, responsible for dynamically selecting the optimal communication mode (5G, Mesh, Satellite, etc.) based on real-time analysis of the security posture, connectivity quality, mission requirements, and threat level.
*   **Secure 5G Module**: A hardened 5G communication stack featuring IMSI privacy, base station authentication, double encryption, and traffic obfuscation to counter 5G-specific threats.
*   **Enhanced Mesh Communication**: Built on the conceptual foundation of BitChat, this module includes advanced features like onion routing for privacy, a dynamic `RelayPathManager` for selecting optimal and secure message paths, and a `Proof-of-Relay` protocol to ensure node integrity.
*   **Advanced Communication Modules**: Includes modules for satellite communication and a last-resort emergency radio beacon.
*   **Unified Threat Detection**: A framework that consolidates threat intelligence from all communication modules to provide a holistic view of the threat landscape and orchestrate automated responses.
*   **Autonomous Recovery Protocols**: Failsafe systems designed to detect communication blackouts and execute autonomous recovery procedures, such as activating an emergency beacon or initiating a return-to-launch sequence.

For a comprehensive understanding of the architecture, design decisions, and project plan, please refer to the documents in the `Docs/` directory.

## Prerequisites

*   Python 3.7+
*   The `cryptography` library

## Setup

1.  **Clone the repository or ensure all files are in their respective directories.**

2.  **Install the required Python library.**
    Open your terminal or command prompt and run the following command:
    ```sh
    pip install cryptography
    ```

## Running the Simulations

The primary entry points for running the simulations are located in the `main_simulations/` directory. Each file is designed to run independently and demonstrates a specific aspect of the Cerberus v0.3 system.

---

### 1. Main Communication Manager Simulation

This simulation demonstrates the core decision-making loop of the `CommunicationManager`, which dynamically switches between communication modes based on simulated environmental factors.

**To run:**
```sh
python3 main_simulations/main_communication_manager_simulation.py
```

---

### 2. Enhanced Mesh Communication Simulation

This simulation showcases the advanced mesh networking capabilities, including the `RelayPathManager` selecting an optimal path, `OnionRouting` for message privacy, and `ProofOfRelay` for verifying node behavior.

**To run:**
```sh
python3 main_simulations/main_mesh_simulation.py
```

---

### 3. Secure 5G Communication Simulation

This simulation demonstrates the hardened 5G module in action. It runs through scenarios including a legitimate connection, detecting a fake base station, and responding to simulated threats like protocol downgrade attacks and IMSI catchers.

**To run:**
```sh
python3 main_simulations/main_5g_simulation.py
```

---

### 4. Advanced Communication and Threat Detection Simulation

This simulation demonstrates the integration of satellite and emergency beacon modules, as well as the `UnifiedThreatDetectionFramework` and `AutonomousRecoveryProtocols`. It simulates multi-source threat detection and a full communication blackout scenario.

**To run:**
```sh
python3 main_simulations/main_advanced_communication_simulation.py
```

---

### 5. Testing and Operationalization Simulation

This simulation demonstrates the testing frameworks. It runs a series of adversarial security tests and showcases the logic for handling communication blackouts and initiating autonomous recovery.

**To run:**
```sh
python3 main_simulations/main_testing_operationalization_simulation.py
```

## Codebase Structure

The project is organized into the following key directories:

*   `communication/`: Contains the core communication modules, including the main `CommunicationManager`.
*   `Docs/`: All project documentation, including architectural overviews, feasibility analysis, project plans, and suggestions.
*   `main_simulations/`: Executable scripts to run demonstrations of different parts of the system.
*   `operational/`: Modules related to operational procedures and compliance.
*   `protocols/`: High-level protocols for autonomous recovery, performance optimization, and blackout detection.
*   `security/`: Implementation of various security components and threat detectors.
*   `testing/`: Frameworks for adversarial security testing and field test simulations.