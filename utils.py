def dollar_formatter(x, pos):
    return f'${x:,.0f}'

def adjust_for_inflation(df, inflation_series):
    """Adjust values to base year dollars using inflation rates."""

    # we use cumprod on (1 + rate) to compound the interest backward from base_year
    multipliers = (1 + inflation_series).cumprod()
    
    # shift and fill so the base_year multiplier is exactly 1.0
    multipliers = multipliers.shift(1, fill_value=1.0)

    # map the multipliers to the main dataframe and multiply
    df['multiplier'] = df['year'].astype(str).map(multipliers)
    df['value_adjusted'] = df['value'] * df['multiplier']
    
    return df
