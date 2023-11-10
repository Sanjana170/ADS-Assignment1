# Import pandas library as visuals
import pandas as visuals

# Import matplotlib library as visualpyp
import matplotlib.pyplot as visualpyp

# Read population data from 'Population.xlsx' file and store it in the 'Population' variable
Population = visuals.read_excel("Population.xlsx")

# Display the population data
print(Population)

# Read CO2 emission data from 'CO2 emission.xlsx' file and store it in the 'Co2_emission' variable
Co2_emission = visuals.read_excel("CO2 emission.xlsx")

# Display the CO2 emission data
print(Co2_emission)

# Set index of the 'Population' dataframe to 'Country Name' column and store it in the 'Population1' variable
Population1 = Population.set_index("Country Name")

# Function to create a line plot of population data for a specific country
def Visualization_1(data, titles):
    # Create a figure with specified size
    visualpyp.figure(figsize=(20, 6))

    # Plot the population data for the input country
    visualpyp.plot(
        list(range(2001, 2021)), list(data.loc["Germany"]), color="red", label="Germany"
    )
    visualpyp.plot(
        list(range(2001, 2021)), list(data.loc["India"]), color="blue", label="India"
    )
    visualpyp.plot(
        list(range(2001, 2021)),
        list(data.loc["Afghanistan"]),
        color="green",
        label="Afghanistan",
    )

    # Set labels for the x and y axes
    visualpyp.xlabel("Year")
    visualpyp.ylabel("value")

    # Set the title of the plot
    visualpyp.title(titles)

    # Add a legend to the plot
    visualpyp.legend(["Germany", "India", "Afghanistan"])

    # Rotate x-axis labels for better readability
    visualpyp.xticks(rotation=90)

    # Display the plot
    visualpyp.show()


# Call the Visualization_1 function to plot population details for Germany, India, and Afghanistan
Visualization_1(data=Population1, titles="Population details 2001-2020 yearwise")

# Set index of the 'Co2_emission' dataframe to 'Country Name' column and store it in the 'Co2_emission1' variable
Co2_emission1 = Co2_emission.set_index("Country Name")

# Call the Visualization_1 function to plot CO2 emission details for Germany, India, and Afghanistan
Visualization_1(data=Co2_emission1, titles="Co2_emission details 2001-2020 yearwise")

# Function to create scatter plots of population vs. CO2 emission for a specific country
def Visualization_2(county_name):
    # Create a figure with specified size
    visualpyp.figure(figsize=(9, 5))

    # Extract population and CO2 emission data for the input country
    population_data_country = Population1.loc[county_name]
    co2_emission_data_country = Co2_emission1.loc[county_name]

    # Create a scatter plot for 2001-2010 with red color
    visualpyp.scatter(
        population_data_country[:10], co2_emission_data_country[:10], s=40, c="red"
    )

    # Set labels for the x and y axes
    visualpyp.xlabel("population")
    visualpyp.ylabel("Co2_emission")

    # Set the title of the plot
    visualpyp.title(
        county_name + " country's population Vs Co2_emission for 2001- 2010 years"
    )

    # Rotate x-axis labels for better readability
    visualpyp.xticks(rotation=90)

    # Display the plot
    visualpyp.show()

    # Create another figure with specified size
    visualpyp.figure(figsize=(9, 5))

    # Create a scatter plot for 2010-2020 with green color
    visualpyp.scatter(
        population_data_country[-10:], co2_emission_data_country[-10:], s=40, c="green"
    )

    # Set labels for the x and y axes
    visualpyp.xlabel("population")
    visualpyp.ylabel("Co2_emission")

    # Set the title of the plot
    visual
