# BitChat Overview

BitChat is a decentralized peer-to-peer messaging app that works over Bluetooth mesh networks. It requires no internet, no servers, and no phone numbers, aiming to be a secure and private alternative to traditional messaging apps.

## Key Features:

*   **Decentralized Mesh Network**: Automatic peer discovery and multi-hop message relay over Bluetooth LE.
*   **Privacy First**: No accounts, no phone numbers, no persistent identifiers.
*   **Private Message End-to-End Encryption**: Uses Noise Protocol.
*   **IRC-Style Commands**: Familiar `/slap`, `/msg`, `/who` style interface.
*   **Universal App**: Native support for iOS and macOS.
*   **Emergency Wipe**: Triple-tap to instantly clear all data.
*   **Performance Optimizations**: LZ4 message compression, adaptive battery modes, and optimized networking.

## Technical Details:

*   **Binary Protocol**: Efficient binary protocol optimized for Bluetooth LE with compact packet format, TTL-based message routing (max 7 hops), automatic fragmentation, and message deduplication.
*   **Mesh Networking**: Each device acts as both client and peripheral, with automatic peer discovery and connection management, and adaptive duty cycling for battery optimization.

## Setup Options:

*   **XcodeGen (Recommended)**: `brew install xcodegen`, then `cd bitchat` and `xcodegen generate`, then `open bitchat.xcodeproj`.
*   **Swift Package Manager**: `cd bitchat` and `open Package.swift`.
*   **Manual Xcode Project**: Create new iOS/macOS App in Xcode, copy Swift files, update Info.plist with Bluetooth permissions, set deployment target to iOS 16.0 / macOS 13.0.
*   **just**: `just run` to set up and run on macOS from source, `just clean` to restore.

## Warning:

Private messages have not received external security review and may contain vulnerabilities. Do not use for sensitive use cases, and do not rely on its security until it has been reviewed. Public local chat (the main feature) has no security concerns.

