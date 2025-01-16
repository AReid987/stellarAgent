---
type: Idea
title: Haystack RAG - Stellar SDK
tags: [RAG, Haystack, StellarSDK]
---

[Guide: Stellar SDK Integration](https://app.capacities.io/home/5b4aa90c-9468-43e3-b5d5-1d6477ab3edc)

# Haystack RAG - Stellar SDK

To integrate the Stellar SDK and Horizon API for enabling an AI Agent to autonomously create custom assets on the Stellar blockchain, you can follow these steps:

1. **Set Up the Stellar SDK**:

    - Use the Stellar SDK in your preferred programming language to interact with the Stellar network.

        - (JavaScript, Python, Java, or Go)

    - Initialize the SDK and connect to the Horizon server

        - Acts as the API for the Stellar network .

2. **Generate Keypairs**:

    - Create keypairs for the issuer and distributor accounts.

    - The issuer account will create the asset

    - the distributor account will handle the distribution of the asset .

3. **Create the Asset**:

    - Define the asset using the Stellar SDK

        - combine the asset code and the issuer's public key.

        - This creates a unique asset object on the network .

4. **Establish Trustlines**:

    - The distributor account must establish a trustline with the issuer account to hold the asset.

    - This involves using the `changeTrust` operation to set up the trustline with the specified asset and limit .

5. **Authorize Trustlines**:

    - If the authorization flag is enabled

        - the issuer account must approve the distributor account's trustline request before any payments can be made .

6. **Issue the Asset**:

    - Use the `payment` operation to send the specified amount of the asset from the issuer to the distributor account.

    - This operation effectively mints the asset on the network .

7. **Lock the Issuer Account (Optional)**:

    - If you want to limit the supply of the asset permanently

        - you can lock the issuer account using the `setOptions` operation to set the master weight to zero.

        - This prevents any further minting of the asset

By following these steps, you can programmatically create and manage custom assets on the Stellar blockchain using the Stellar SDK and Horizon API.
