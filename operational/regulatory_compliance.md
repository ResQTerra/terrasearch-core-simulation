
# Regulatory Compliance for Cerberus v0.3

This document outlines the regulatory considerations for the Cerberus v0.3 system.

## 1. Spectrum Management

The system utilizes several frequency bands, each with its own regulatory requirements:

- **5G:** Operation is subject to the regulations of the national telecommunications authorities in the country of operation. All 5G modems must be certified for use in the specific bands allocated by the carrier.
- **Bluetooth LE (Mesh):** Operates in the 2.4 GHz ISM band, which is generally license-free. However, devices must comply with power limits and other technical requirements set by bodies like the FCC (in the US) and ETSI (in Europe).
- **Satellite:** Use of satellite communications requires agreements with the satellite operator and is subject to international and national regulations.
- **Emergency Beacon (433 MHz):** The 433 MHz frequency is often used for low-power devices and may have specific regulations regarding duty cycle and power output.

## 2. Export Control

The Cerberus v0.3 system, particularly its advanced encryption and autonomous decision-making capabilities, may be subject to export control regulations such as the U.S. Export Administration Regulations (EAR) or International Traffic in Arms Regulations (ITAR).

A thorough classification of the system's hardware and software components is required to determine the applicable controls.

## 3. Aviation Regulations

As the system is designed for use in drone swarms, it is subject to the aviation regulations of the country of operation. This includes regulations from bodies like the FAA (in the US) and EASA (in Europe) regarding:

- Beyond Visual Line of Sight (BVLOS) operations
- Command and Control (C2) link requirements
- Autonomous operations

## 4. Data Privacy

While the system is designed to be privacy-preserving, the collection of any data that could be considered personal information must comply with data privacy regulations such as GDPR or CCPA.
