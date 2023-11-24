# Nathan Adkins 
# npa0003@mix.wvu.edu
import os
import csv
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np

def parse_csv_file(file_path):   
    per_year_score_dict = dict()
    with open (file_path, 'r') as file:
        csvfile = csv.reader(file)
        next(csvfile)
        for line in csvfile:
            if line:
                per_year_score_dict[line[0]] = float(line[-1])
    return per_year_score_dict

def remove_file_extension(file_path):
    return os.path.splitext(os.path.basename(file_path))[0]

def normalize_scores(scores: dict):
    max_score = max(scores.values())
    return {year: score / max_score for year, score in scores.items()}

def remove_digits(value):
    result_str = f"{value:.2f}"
    return float(result_str)

def points_data():
    team_names = ['Mountaineer Robotics','Team Mountaineers']
    text_file_directory = "urc_data/csv"
    score_dict = dict()
    for csv_file in os.listdir(text_file_directory):
            csv_file_path = os.path.join(text_file_directory, csv_file)
            if os.path.isfile(csv_file_path):
                year = remove_file_extension(csv_file)
                score_dict[year] = parse_csv_file(csv_file_path)

    colors = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
    normalized_scores = dict()
    for year in score_dict:
            normalized_scores[year] = normalize_scores(score_dict[year])

    team_scores = dict()
    normalized_team_score_values = [] 
    for year in sorted(score_dict.keys()):
        scores = normalized_scores[year]
        color = next(colors)
        plt.scatter([year] * len(scores), list(scores.values()), label=year, color=color)

        for key in list(scores.keys()):
            for name in team_names:
                if key == name:
                    normalized_team_score_values.append(scores[key])
                    team_scores[key] = scores[key]
                    plt.text(year, scores[key], f"  our team: ({score_dict[year][key]} pts)", fontsize=12, ha='left', va='center', color='black')
            plt.plot([year, year], [scores[key], scores[key]], color='black', linestyle='--')

    plt.title('Normalized Final Scores: Univerity Rover Challenge (2014-2023)', fontweight='bold')
    plt.xlabel('Year', fontweight='bold')
    plt.ylabel('Normalized Score', fontweight='bold')
    plt.yticks([0] + [remove_digits(val) for val in normalized_team_score_values ])
    plt.ylabel('')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.show()

def extrapolated_data():
    
    years_original = np.array([2022, 2023])
    scores_original = np.array([268.67, 425.35])
    
    # Fit a single line to the original data
    a, b = np.polyfit(years_original, scores_original, 1)
    
    # Extend the line for the next two years
    years_extended = np.array([2024])
    
    # Combine all years (original and extended)
    all_years = np.concatenate((years_original, years_extended))
    
    # Combine all scores (original and extrapolated)
    all_scores = np.concatenate((scores_original, a * years_extended + b))

    # Plot the original data points with larger dots
    plt.scatter(years_original, scores_original, label='Historical Score', color='blue', s=50, zorder=3)
    
    # Plot the line of best fit for all data points
    plt.plot(all_years, a * all_years + b, color='blue', linewidth=1, linestyle='dotted')

    # Plot the extrapolated data points with larger dots
    plt.scatter(years_extended, a * years_extended + b, label="Expected Score", color='red', s=50, zorder=5)

    plt.axhline(y=500, color='orange', linestyle='dashed')
    plt.text(2023, 510, 'Maximum Possible Points', fontsize=10, ha='right', va='bottom', color='orange')


    plt.text(all_years[2],(a * all_years[2] + b) - 8,f'  {a * all_years[2] + b:.1f} pts')
    # plt.text(all_years[3] + 0.1,(a * all_years[3] + b) - 8,f'{a * all_years[3] + b:.1f} pts')

    plt.xticks(np.arange(2022, 2025, 1))
    
    plt.title('Team Mountaineers: Expected Final Score for 2024', fontweight='bold')
    plt.xlabel('Competition Year', fontweight='bold')
    plt.ylabel('Final Score', fontweight='bold')
    plt.legend()
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.ylim(0, 600)
    plt.show()



def main():
    
    # points_data()
    extrapolated_data()



if  __name__ == '__main__':
    main()
