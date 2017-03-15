import pandas as pd

def preprocess_features(data):
    ''' 
    Preprocesses input data. 
    converts non-numeric binary variables into
    binary (0/1) variables. 
    Converts categorical variables into dummy variables. 
    '''
    output = pd.DataFrame(index = data.index)

    # Investigate each feature column for the data
    for col, col_data in data.iteritems():
        
        # If data type is non-numeric, replace all yes/no values with 1/0
        if col_data.dtype == object:
            col_data = col_data.replace(['yes', 'no'], [1, 0])

        # If data type is categorical, convert to dummy variables
        if col_data.dtype == object:
            col_data = pd.get_dummies(col_data, prefix = col)  
        
        # Collect the revised columns
        output = output.join(col_data)
        # Unify all column names by transforming to lower case
        output.columns = output.columns.str.lower()
    
    return output


def discrete_charts(data, cols, plot_color):
    from bokeh.charts import Bar, output_file, show
    from bokeh.io import output_notebook
    from bokeh.plotting import figure
    from bokeh.layouts import gridplot
    from bokeh.layouts import column, row
    from bokeh.plotting import reset_output
    from bokeh.charts.attributes import cat
    from collections import Counter
    from IPython.display import display
    col_dict = {}
    
    for col in cols:
        col_dict[col] = pd.DataFrame.from_dict(Counter(data[col]), orient='index')
        col_dict[col].columns = [col]


    
    row_coll = []
    rows = []
    block = True

    for column in cols:
        block = True
        column_title_split = column.split('_')
        column_title = ""
        for column_title_piece in column_title_split:
            column_title += " " +column_title_piece.title()
        
        p = Bar(col_dict[column], 
                values=column, 
                title=column_title + ' Stats',
                color=plot_color,
                plot_width=300, 
                plot_height=200,
                ylabel="",
                legend=None,
                toolbar_location=None)
        rows.append(p)
        if len(rows) == 3:
            block = False
            row_coll.append(list(rows))
            reset_output()
            rows = []

    if block:
        row_coll.append(list(rows))
        
    #print row_coll
    gridplot = gridplot(row_coll)
    output_notebook()
    show(gridplot)

def discrete_dept_charts(data, plot_color):
    from bokeh.charts import Bar, output_file, show
    from bokeh.io import output_notebook
    from bokeh.plotting import figure
    from bokeh.layouts import gridplot
    from bokeh.layouts import column, row
    from bokeh.plotting import reset_output
    from bokeh.charts.attributes import cat
    from collections import Counter
    from IPython.display import display
    row_coll = []
    rows = []
    counter = 1

    for column in data.columns:
        column_title_split = column.split('_')
        column_title = ""
        for column_title_piece in column_title_split:
            column_title += " " +column_title_piece.title()
        
        p = Bar(data, 
                values=column, 
                title='Average' + column_title + ' by department',
                color=plot_color,
                plot_width=300, 
                plot_height=200,
                ylabel="",
                legend=None,
                toolbar_location=None)
        rows.append(p)
        if len(rows) == 3:
            row_coll.append(list(rows))
            reset_output()
            rows = []
        
    row_coll.append(list(rows))
        
    gridplot = gridplot(row_coll)
    output_notebook()
    show(gridplot)