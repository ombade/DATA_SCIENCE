#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<string> teams;

    cout << "Enter team names (enter 'q' to stop):\n";
    while (true) {
        string team;
        cin >> team;
        if (team == "q") {
            break;
        }
        teams.push_back(team);
    }

    int numTeams = teams.size();
    if (numTeams < 3 || numTeams > 10) {
        cout << "Invalid number of teams." << endl;
    } else {
        for (int i = 0; i < numTeams; ++i) {
            for (int j = i + 1; j < numTeams; ++j) {
                cout << teams[i] << "-VS-" << teams[j] << " ";
            }
        }
        cout << endl;
    }

    return 0;
}
