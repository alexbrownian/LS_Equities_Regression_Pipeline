# =============================================================
# Long/Short Equity Pipeline — Configuration
# Edit this file to change the stock universe and parameters.
# =============================================================

# ── Stock Universe ────────────────────────────────────────────
LONG_CANDIDATE = "GEVO"          # Stock you are long

SHORT_CANDIDATES = [              # Basket of short candidates
    "CHPT",   # ChargePoint - EV charging cash incinerator, no profitability path
    "BE",     # Bloom Energy - poor unit economics, negative FCF
    "RUN",    # Sunrun - rate-sensitive balance sheet, high leverage
    "ARRY",   # Array Technologies - margin squeeze from Chinese competition
    "HYLN",   # Hyliion - pre-revenue, missed timelines
    "RIVN",   # Rivian - ~$5-6B/yr cash burn, repeated dilutive raises
    "LCID",   # Lucid Group - terminal unit economics, ~$28K revenue vs ~$100K+ cost/car
    "GOEV",   # Canoo - near-zero revenue, serial dilution, going-concern
    "ALTO",   # Alto Ingredients - commodity ethanol, zero carbon differentiation
    "REI",    # Ring Energy - leveraged conventional oil, no transition optionality
    "PARR",   # Par Pacific - high-cost refining, no SAF/renewable conversionn
    "AFRM",   # Affirm - BNPL credit losses accelerate in any consumer softening
    "GPRE",   # Green Plains - ethanol price taker, no CCS or carbon differentiation
    "PLUG",   # Plug Power - hydrogen hype, persistent negative gross margins
    "AMTX",   # Aemetis - pre-profit biofuel, inferior assets vs Gevo, missed milestones
]

# ── Benchmarks ────────────────────────────────────────────────
SECTOR_ETF   = "XLK"             # Sector ETF matching your universe
MARKET_INDEX = "SPY"             # Broad market index

# ── Time Parameters ───────────────────────────────────────────
LOOKBACK_YEARS       = 5         # Years of history to pull
REBALANCE_FREQ       = "M"       # Rebalancing: 'D', 'W', 'M', 'Q'
FORWARD_RETURN_DAYS  = 21        # Prediction horizon (~1 month)

# ── Risk Parameters ───────────────────────────────────────────
RISK_FREE_RATE      = 0.05       # Annual risk-free rate
TARGET_VOLATILITY   = 0.15       # Annual portfolio vol target
MAX_STOCK_WEIGHT    = 0.40       # Max absolute weight, single stock
MAX_SECTOR_CONC     = 0.40       # Max sector concentration

# ── ML Parameters ─────────────────────────────────────────────
ML_TRAIN_FRAC = 0.70             # Train / test split fraction
N_CV_FOLDS    = 5                # Cross-validation folds
RANDOM_STATE  = 42

# ── Signal / Backtest Parameters ──────────────────────────────
ZSCORE_ENTRY         = 2.0       # Z-score threshold to enter
ZSCORE_EXIT          = 0.5       # Z-score threshold to exit
ZSCORE_WINDOW        = 60        # Rolling window for z-score (days)
TRANSACTION_COST_BPS = 5         # One-way transaction cost (bps)

# ── Directories ───────────────────────────────────────────────
DATA_DIR   = "data/"
OUTPUT_DIR = "outputs/"
