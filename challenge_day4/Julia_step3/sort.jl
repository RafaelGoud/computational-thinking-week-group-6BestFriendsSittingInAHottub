using DataFrames, CSV, Statistics, DelimitedFiles

# Read the CSV file into a DataFrame (testdata is in the parent challenge_day4 folder)
people_df = CSV.File(joinpath(@__DIR__, "..", "testdata", "data3.csv")) |> DataFrame

# Function to classify a score based on quartiles
function classify_score(score, quartiles)
    if score <= quartiles[1]
        return "low"
    elseif score <= quartiles[2]
        return "middle"
    elseif score <= quartiles[3]
        return "good"
    else
        return "super"
    end
end

# Iterate over each column (skipping the 'name' column)
for col_name in names(people_df)[2:end]
    # Normalize numeric values: convert Float64 whole numbers to Int, keep missings/strings
    col_data = map(x -> (x === missing) ? missing : (x isa Float64 && x == floor(x) ? Int(x) : x), people_df[!, col_name])

    # Collect numeric values for quartiles (as Float64)
    numeric_vals = [Float64(x) for x in col_data if x isa Number && x !== missing]

    if isempty(numeric_vals)
        println("No valid numeric data for column $col_name")
        continue
    end

    quartiles = quantile(numeric_vals, [0.25, 0.5, 0.75])

    # Replace numeric values with categories; leave missing as missing and non-numeric as "low"
    new_col = map(x -> x === missing ? missing : (x isa Number ? classify_score(Float64(x), quartiles) : "low"), col_data)
    people_df[!, col_name] = new_col
end

# Save the modified DataFrame back to a new CSV file next to the original testdata
CSV.write(joinpath(@__DIR__, "..", "testdata", "data4.csv"), people_df)

# Save the modified DataFrame back to a new TXT file
writedlm(joinpath(@__DIR__, "..", "fulldata", "data3.txt"), people_df, ',')