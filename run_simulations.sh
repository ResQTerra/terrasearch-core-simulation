#!/bin/bash

# A script to run the Cerberus v0.3 simulations.
# It provides a menu for easy selection of individual simulations or running all of them.

# Define colors for better output formatting
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to display the main menu
show_menu() {
    echo -e "${BLUE}====================================================${NC}"
    echo -e "${YELLOW}       Cerberus v0.3 Simulation Runner Menu       ${NC}"
    echo -e "${BLUE}====================================================${NC}"
    echo "Please choose a simulation to run:"
    echo "  1) Main Communication Manager Simulation"
    echo "  2) Enhanced Mesh Communication Simulation"
    echo "  3) Secure 5G Communication Simulation"
    echo "  4) Advanced Communication and Threat Detection Simulation"
    echo "  5) Testing and Operationalization Simulation"
    echo ""
    echo -e "  ${GREEN}a) Run ALL simulations in sequence${NC}"
    echo "  q) Quit"
    echo -e "${BLUE}----------------------------------------------------${NC}"
}

# Function to run a specific simulation
run_simulation() {
    local script_name="$1"
    local description="$2"
    
    echo -e "\n${GREEN}>>> Running: $description...${NC}"
    echo -e "${BLUE}----------------------------------------------------${NC}"
    
    # Check if the file exists before trying to run it
    if [ -f "main_simulations/$script_name" ]; then
        python3 "main_simulations/$script_name"
    else
        echo -e "\n${RED}ERROR: Could not find script 'main_simulations/$script_name'${NC}"
    fi
    
    echo -e "${BLUE}----------------------------------------------------${NC}"
    echo -e "${GREEN}<<< Finished: $description${NC}"
    echo -e "\nPress Enter to return to the menu..."
    read
}

# Main loop to display the menu and handle user input
while true; do
    clear
    show_menu
    read -p "Enter your choice [1-5, a, q]: " choice

    case $choice in
        1)
            run_simulation "main_communication_manager_simulation.py" "Main Communication Manager Simulation"
            ;;
        2)
            run_simulation "main_mesh_simulation.py" "Enhanced Mesh Communication Simulation"
            ;;
        3)
            run_simulation "main_5g_simulation.py" "Secure 5G Communication Simulation"
            ;;
        4)
            run_simulation "main_advanced_communication_simulation.py" "Advanced Communication and Threat Detection Simulation"
            ;;
        5)
            run_simulation "main_testing_operationalization_simulation.py" "Testing and Operationalization Simulation"
            ;;
        a|A)
            echo -e "\n${GREEN}>>> Running ALL simulations in sequence...${NC}"
            
            # Define an array of scripts and descriptions
            scripts=("main_communication_manager_simulation.py" "main_mesh_simulation.py" "main_5g_simulation.py" "main_advanced_communication_simulation.py" "main_testing_operationalization_simulation.py")
            descriptions=("Main Communication Manager" "Enhanced Mesh Communication" "Secure 5G Communication" "Advanced Communication and Threat Detection" "Testing and Operationalization")

            for i in "${!scripts[@]}"; do
                echo -e "\n${YELLOW}--- Starting [${descriptions[$i]}] ---${NC}"
                python3 "main_simulations/${scripts[$i]}"
                echo -e "${YELLOW}--- Finished [${descriptions[$i]}] ---${NC}"
                # Pause between simulations to make output readable
                if [ $i -lt $((${#scripts[@]}-1)) ]; then
                    echo "Pausing for 3 seconds..."
                    sleep 3
                fi
            done
            
            echo -e "\n${GREEN}<<< All simulations complete.${NC}"
            echo -e "\nPress Enter to return to the menu..."
            read
            ;;
        q|Q)
            echo "Exiting."
            break
            ;;
        *)
            echo "Invalid choice. Please select a valid option."
            echo "Press Enter to continue..."
            read
            ;;
    esac
done