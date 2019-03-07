def raw_column_filter(in_df):

    target_cols = ['INCTOT','INCWAGE', 'WKXPNS','OCC','OCCLY','REGION', 'METAREA', 'STATEFIP', 'MIGSTA1', 'AGE',
    'UHRSWORKT','EDUC', 'WHYMOVE', 'ASECWT', 'ASECWTH']

    renamed_cols = ['total_income','wage_income','work_expenses','occupation','occupation_ly','region','met_area','state',
                   'state_ly','age','usual_hours_work','education','move_reason','asec_wt','asec_wt_h']

    out_df = in_df[target_cols]
    out_df.columns = renamed_cols
    return out_df


def find_computer_occupations(in_df):
    #TODO: ADD OCCUPATION CODE 0110
    out_df = in_df[in_df.occupation<=1107]
    out_df = out_df[out_df.occupation>=1000]
    return out_df

# def find_top_5_tech_states(in_df):

#     out_df = in_df[in_df.state.isin([36,6,48,53,34]) ]
#     return out_df

def filter_incomes_codes(in_df):
    out_df = in_df[in_df.total_income!=0]
    out_df = out_df[out_df.total_income < 999999]
    return out_df

def get_region_dummies(in_df):
    simple_regions = in_df.region.apply(lambda x: str(x)[0]).astype('category')
    simple_regions = simple_regions.map( {'1':'north',
                                          '2': 'midwest',
                                          '3': 'south',
                                          '4': 'west',}
                                        )
    out_df = in_df
    out_df['simple_regions'] = simple_regions
    dummies = pd.get_dummies(simple_regions, prefix='in')
    return dummies


def get_state_dummies(in_df):
    state_cats = in_df.state.astype('category')
    dummies = pd.get_dummies(state_cats, prefix='in')
    return dummies

def get_education_dummies(in_df):
    educ_cats = in_df.education.astype('category')
#     educ_cats = educ_cats.map({
#         '123':
#         '124':
#         '125'
#     })
    dummies = pd.get_dummies(educ_cats, prefix='level')
    return dummies
def get_intech_dummy(in_df):
    out_df = in_df.occupation.isin(range(1000,1108))
    return out_df

#def get_moved_ly()
# def create_state_dummies(in_df):
#     in_df['state' in['06','CA','TX']
def append_all_dummies(in_df):
    return pd.concat([in_df,get_region_dummies(in_df),get_state_dummies(in_df), get_intech_dummy(in_df),get_education_dummies(in_df),],axis=1)
