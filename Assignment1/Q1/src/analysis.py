import pandas as pd
import scipy.stats as stats

# T-test will show statistical significance between two groups
def t_test(file_path, output_file):
    # Read CSV into a df
    df = pd.read_csv(file_path)
    
    # Store results in a list
    results = []
    
    # Go through all number cols in the df
    for column in df.select_dtypes(include=['number']).columns:
        # Separate the data into two groups based on frailty
        group_N = df[df['Frailty'] == 'N'][column]
        group_Y = df[df['Frailty'] == 'Y'][column]
        
        # Do the two-sample t-test
        t_stat, p_value = stats.ttest_ind(group_N, group_Y, equal_var=False)
        
        # Append results to the results list
        results.append([column, t_stat, p_value])
    
    # Convert the results list into a df
    results_df = pd.DataFrame(results, columns=["Column", "T-statistic", "P-value"])
    
    # Save the df to a the test_results.txt file
    results_df.to_string(output_file, index=False)
    
    print(f"Results saved to {output_file}")

t_test('Q1/data_clean/clean_frailty_data.csv', 'Q1/results/test_results.txt')