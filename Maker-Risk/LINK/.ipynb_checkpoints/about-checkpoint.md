# Chainlink resources 

## Internal MakerDAO

Internal MakerDAO resources: 
- [Collateral index list](https://forum.makerdao.com/t/collateral-status-index/2231/20)
- [Link collateral application](https://forum.makerdao.com/t/link-collateral-onboarding-application/2586)
- [LINK Risk Parameter RFC](https://forum.makerdao.com/t/link-risk-parameter-request-for-comment/2118)

Oracles: 
- [Chainlink oracles for LINK-USD](https://forum.makerdao.com/t/using-chainlink-oracles-for-link-usd/2670)
- [Oracle comparisons: LINK, MKR](https://forum.makerdao.com/t/using-chainlink-oracles-for-link-usd/2670/14)

Community/governance:
- [Action on state of peg](https://forum.makerdao.com/t/action-required-state-of-the-peg/2025)
- [Community vote LINK](https://forum.makerdao.com/t/action-required-state-of-the-peg/2025/51)

## Project and external 

- [Chainlink website]()
- [Chainlink whitepaper](https://link.smartcontract.com/whitepaper)
- [Chainlink documentation](https://docs.chain.link/docs)
- [Source code](https://github.com/smartcontractkit/chainlink)
- [Token etherscan](https://etherscan.io/token/0x514910771af9ca656af840dff83e8264ecf986ca)
- [Awesome Chainlink Github](https://github.com/JohannEid/awesome-chainlink)

- [Chainlink node operator list](https://market.link/search/nodes)
- [Chainlink oracle reputation list](https://reputation.link/)
- [LINK/USD feed](https://feeds.chain.link/link-usd)

External reports: 
- [Zeus Capital report on LINK](https://chainlink.docsend.com/view/nfrvnyuuzrf2d5va)
    - [Chainlink comment on report](https://forum.makerdao.com/t/using-chainlink-oracles-for-link-usd/2670/19)


Smart contract audits: 
- Nick Johnson Audit Report: [Audit](https://github.com/smartcontractkit/audits/blob/master/reports/Nick%20Johnson%20-%20Chainlink%20Audit%20Report.pdf)
- Quantstamp Audit Report: [Audit](https://github.com/smartcontractkit/audits/blob/master/reports/Quantstamp%20-%20Chainlink%20Audit%20Report.pdf)
- SigmaPrime Audit Report: [Audit](https://github.com/smartcontractkit/audits/blob/master/reports/SigmaPrime%20-%20Chainlink%20Smart%20Contract%20Security%20Review.pdf)

Community links: 
- Twitter: https://twitter.com/chainlink
- Reddit: https://www.reddit.com/r/Chainlink/
- Telegram: https://t.me/chainlinkofficial
- Discord: https://discord.gg/aSK4zew

# Application: 

- Source: [Link collateral application](https://forum.makerdao.com/t/link-collateral-onboarding-application/2586)

What is chainlink: 

Chainlink is a generalized blockchain agnostic framework for **building decentralized oracle networks** that provide smart contracts with tamper-resistant access to real world data, events, and payments that reside on off-chain systems.

Token use:

The LINK token is used to **pay node operators for delivering off-chain data/compute** through LINK’s ERC677 (ERC20 compliant) **transferAndCall() function**. LINK will also be **staked by node operators in service level agreements** (SLAs) as collateral which can be slashed for malicious activity, unresponsiveness, or any other predefined condition in the SLA

Token distribution: 

**SmartContract retains roughly 27% of the total supply** of 1,000,000,000 LINK tokens out of an initial 30% allocation. SmartContract also controls an additional 35% of the token supply that is allocated to **incentives for node operators**. Roughly **38% of supply is circulating** (35% from the initial token sale and 3% from SmartContract sales/dispositions).

Project: 

Chainlink had a token sale in September 2017 with a cap of $32M. The Chainlink mainnet was launched in **May 2019 with an ETH/USD reference price** feed. Since then, there are now 30+ price feeds connected with 16 DeFi projects.

How collateral used: 

(other than node payment and staking)

LINK is also used as a collateral asset, representing **34% of Aave’s total market size** ($23M of $67M) and 40% of Aave’s total value locked ($22M of $54M) as of 21 May 2020.

Legal responsibility: 

No organization bears legal responsibility for the collateral. The token is open source and permissionless, with no blacklisting/whitelisting or minting functionality.

SmartContract retains roughly 27% of the total supply of LINK tokens, and including the 35% reserved for node operator rewards retains **effective control of roughly 62% of total token suppl**y. It looks like the ICO and company token holdings are managed through **SmartContract Chainlink Ltd SEZC**, which is registered in the Cayman Islands. SmartContract’s primary place of business is in the US state of California.

Exchanges: 

LINK is traded on centralized exchanges including **Coinbase, Binance, Kraken, Gemini, Huobi, OKEx, Bittrex**, as well as decentralized platforms such as **Kyber, Uniswap, 0x, Loopring, and Oasis**.

Legal classification: 

This article (https://www.sec.gov/corpfin/framework-investment-contract-analysis-digital-assets) from the SEC may also help frame discussions on the token’s legal classification.

Per the terms of use (https://chain.link/terms), LINK has not been registered with financial regulatory authorities in any jurisdiction. I am not aware of any regulatory actions regarding SmartContract or the LINK token.

Oracle data sources (LINK): 

The centralized exchanges listed have LINK/USD: **Coinbase, Binance, Kraken, Gemini, Huobi, OKEx, Bittrex**..

Chainlink also has a **LINK/USD price feed live on mainnet**. It is **updated every 1% price deviation** by 9 independent security reviewed nodes connected to multiple price data aggregators such as BraveNewCoin (feeds data to bloomberg terminal), Coingecko, and Kaiko.


# Using oracles (maker)

- Source: [Using Chainlink Oracles](https://forum.makerdao.com/t/using-chainlink-oracles-for-link-usd/2670)

oracle = node operator


Price feed ecosystem: 

Chainlink’s decentralized oracle networks provide on-chain price feeds. The price feed is a smart contract deployed on Ethereum which medianizes price values coming from independent node operators

oracles (aka node operators) and data providers together form the basis of Chainlink’s decentralized oracle network’s security

**Node operators**

Node operators are **entities responsible for running Ethereum and Chainlink nodes** and maintaining credentials for API providers that fetch specific data points, such as the price of a crypto asset.

Chainlink ecosystem comprises around a hundred oracles/node operators

Node operators servicing our decentralized oracle networks to generate on-chain price feeds, are a subset of the overall node operator ecosystem. High competency in infrastructure: blockchain infra or data providers turned node operators.

Node operators in Chainlink reference price data networks are sybil resistant and go through both identity and security reviews before being added to networks. This provides transparency to on-chain price feeds contract creator and their users.

These operators are distributed all over the world: drastically reduce the risks associated with specific infrastructure failures in any one region

**Data sources** (aka data aggregators)

The node operators fetch data directly from data aggregator endpoints. We favor using aggregators because there are many inherent **issues that can arise from fetching data directly from exchanges**. e.g. liquidity and volume shifts across exchanges, data manipulation, data source attack vectors

Benefits of data aggregators vs exchanges:

- oracles should rely on data aggregators teams that are experts at creating algorithms that detect data anomalies and volume shifts across markets
- decentralize the data curation process by relying on multiple different calculation methods and algorithms

Examples of data aggregators: 
- The LINK-USD price feed currently uses 7 different data aggregators including BraveNewCoin (https://bravenewcoin.com/ 1), Amberdata(https://amberdata.io/), CoinAPI (https://www.coinapi.io/)
- The amount of data providers can be increased over time as the amount of nodes grows, due to the additional value secured by this oracle network.

**Integration into maker**

Chainlink contracts follow a read model, this makes it simple to integrate them as a source of data in the OSM module

Since LINK and the oracle networks are closely intertwined, it will act as **one wholistic pool of risk**, at least for this specific integration. The risk may indeed even be reduced because a portion of Maker’s collateral will be running on a separate oracle mechanism.


**Oracle implementation**

In Maker OSM, values can be read from any contract that has the `peak() and read()` method implemented

 The Chainlink team will **create a proxy contract** that implements the read(), peek(), peep(), and poke() methods such as
```
interface IDSValue {
function peek() external view returns (bytes32, bool);
function read() external view returns (bytes32);
function peep() external view returns (bytes32, bool);
function poke() external;
}
```

How each function will interact with the Chainlink reference contract(https://docs.chain.link/docs/using-chainlink-reference-contracts#config 2)

- peek(): Returns the current feed value and a boolean indicating whether it is valid.
    - current feed value: The current feed value will correspond to the latest price converted to bytes32 as required by the OSM.
    - boolean: The boolean will correspond to the result of a check for stale data, using the concept of Round updates.
- read(): Returns the current feed value reverts if it was not set by some valid mechanism.
    - current feed value: This will be a simple function that calls the latest price value of Chainlink’s price feed.

[Interaction Maker OSM and Chainlink ref contract via proxy](https://makerdao-forum-backup.s3.dualstack.us-east-1.amazonaws.com/original/2X/c/cd744fb0b2e6353a9f52133a91ce5fd9aafbf755.png)

# 



# Exploratory data analysis

# Model 

(LEND example)

- Loss distribution of portfolio of LINK vaults
- Derive risk parameters from loss distribution
- Inputs: trading data + stressed input param
- Auction parameters


# Example

- [LEND risk analysis](https://forum.makerdao.com/t/lend-mip12c2-sp2-collateral-onboarding-risk-evaluation/3127)