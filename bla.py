# Takes a file CSV file called "data.csv" and outputs each row as a numbered YAML file.
# Data in the first row of the CSV is assumed to be the column heading.

# Import the python library for parsing CSV files.
import csv
import os

# Open our data file in read-mode.
csvfile = open('samples/test.csv', 'r')

# Save a CSV Reader object.
datareader = csv.reader(csvfile, delimiter=',', quotechar='"')

# Empty array for data headings, which we will fill with the first row from our CSV.
data_headings = []


def write_patch_header(yaml_file) :
    yaml_text = "patches:"+"\n"
    yaml_file.write(yaml_text)

def write_entry(yaml_file):
    yaml_text = " "*4 +"-"+"\n"
    new_yaml.write(yaml_text)

def write_selected_patch(yaml_file):
    pass
    
 
# Loop through each row...
for row_index, row in enumerate(datareader):
   
	# If this is the first row, populate our data_headings variable.
    if row_index == 0:
        data_headings = row

    else:
        # Only write approved patches
        if row[0] == "yes" :
            #
            # Try to append to an existing file or create a new one "a" mode.
            #
            if not os.path.exists(row[18] + ".yaml") :
                new_yaml =open(row[18] + ".yaml","w")
                write_patch_header(new_yaml)

            new_yaml = open(row[18] + ".yaml","a")
            
            write_entry(new_yaml)
            yaml_text = " "*8
            # Loop through each cell in this row...
            for cell_index, cell in enumerate(row):

                # Heading text is converted to lowercase. Spaces are converted to underscores and hyphens are removed.
                # In the cell text, line endings are replaced with commas.
                cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
                cell_text = cell_heading + ": '" + cell.replace("\n", ", ") + "'\n"
    
                # Add this line of text to the current YAML string.
                if cell_heading == "id" :
                    yaml_text += cell_text

            # Write our YAML string to the new text file and close it.
            new_yaml.write(yaml_text)   

# We're done! Close the CSV file.
csvfile.close()
new_yaml.close()