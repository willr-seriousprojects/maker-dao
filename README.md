# MakerDAO

## Contents

- [Risk Governance meeting notes](#risk-governance-meetings)
- [Meeting 2019-05-31](#risk-meeting-2019-05-31)
- [Meeting 2019-06-07](#risk-meeting-2019-06-07)
- [Analytics](#analytics)

<a name="risk-governance-meetings" />

## Risk Governance meeting notes

<b name="risk-meeting-2019-05-31" />

### Meeting notes 2019-05-31

Analysis: 
- relationship between eth and dai changed in dynamic
- supply of dai just been reducing
- age of debt has been reducing -> healthy. costs realised
- what is the right relationship between dai price and price movements? (discussion)
- eth has been taken out of collateralisation -> collateralisation ratio increasing -> impact on secondary lending -> more dai drawn out of Compound and other platforms. Note: DSR supposed to balance out the refinancing dynamic

Multi-collateral:
- collateral analysis required: collateral ratio, liquidity, debt ceiling..
- building out piece-by-piece of analysis
- framework
- SF will be different between assets
- DSR will be same between assets

Next steps:
- understanding of asset and its valuation
- evaluate the risks of asset -> build into risk premium of asset
- how fast CDPs are liquidated

<b name="risk-meeting-2019-06-07" />

### Meeting notes 2019-06-07

Analysis: 
- derivatives and lending becoming an important part of the eth<>DAI dynamic
- refinancing from Mkr to 2nd market platforms has reduced. re: SF reduction
- discussion to have: rate changes between lending platforms
- open debt consistently getting lower than closed debt
- min time scale to see changes from SF reflected in data: **3-5 days**. hard to prevent changes in market conditions within the timescale. re:eth movement is a big indicator. important to keep an eye on 2nd market for inventory.
- collateral ratio: decreasing ratio. re: leverage-seeking behaviour. Usually drop in collateral due to drop in eth value. 
- secondary lending rates: 3-5% buffer between maker and 2nd lending. borrow volumes increasing. 

Risk explanation (Cyrus):
- CDP: exposure risk = insolvency of cdp. Probability of liquidation -> how bad is the exposure. **Needs modelling**. 
  + Action: EAD, LGD, ECL notions need to be modelled and base the SF
  + SF needs to reflect frequency
- risk premium: compensation for risk of liquidation
- bad debt: historically all liquidation has been cleared 100%, with no impact in collateral ratio increase. If that wasn't to happen due to some reason (e.g. reputation risk), we have no
- <> likelyhood of cdp being liquidated 
- collateralisation ratio <> mechanics of liquidation auction
- **important** management of changing risk profiles <> asset-based risk <> different distributions of cdps

New collaterals: 
- framework: how we accept new collateral types. suggestions: 
  + perceived safety of collateral
  + correlation to other assets in portfolio
- 3 steps in evaluation: 
  + classificaiton of collateral 
    + bearer vs non-bearer(bearer asset without counterparty risk e.g. bitcoin. non-bearer e.g. security token)
    + equity/bond tokens
  + due diligence report
    + team/tech/token sale/distribution
  + risk analysis
    + factors leading to adverse market conditions e.g. protocol risk, coding practice
    + valuation models for tokens (frameworks exist)
- community involvement:
  + risk modelling
  + dd analysis
    

























