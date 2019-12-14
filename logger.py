class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # (finished) TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        # Or 
        # f = open(self.file_name, "w") then f.write()
        with open(self.file_name, 'w') as f:
            f.write(f"Pop_size: {pop_size}\t Vacc_Percentage: {vacc_percentage}\tVirus Name: {virus_name}\tMortality Rate: {mortality_rate}\t Reproductive Rate: {basic_repro_num}\n")
        f.close()

        # (finished) TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # (finished) NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''

        with open(self.file_name, 'a') as f:
            if did_infect:
                f.write(f"Person ID: {person._id} infects Random Person ID: {random_person._id} \n")
            elif random_person_vacc:
                f.write(f"Person ID: {person._id} didn't infect Random Person ID: {random_person._id} because vaccinated \n")
            elif random_person_sick:
                f.write(f"Person ID: {person._id} didn't infect Random Person ID: {random_person._id} because already sick \n")
            else:
                f.write(f"Person ID: {person._id} faild to infect Random Person ID: {random_person._id} \n")
        f.close()
        
        # (finished) TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        # pass

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''

        with open(self.file_name, 'a') as f:
            if did_die_from_infection:
                f.write(f"Person ID: {person._id} died from infection\n")
            elif not did_die_from_infection:
                f.write(f"Person ID: {person._id} survived infection\n")
        f.close()


        # (finished) TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        # pass

    def log_time_step(self, time_step_number, total_dead,
        total_infected):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        
        with open(self.file_name, 'a') as f:
            f.write(f"Time step number: {time_step_number} total dead: {total_dead} total infected: {total_infected}\n")

    def log_percentage(self, pop_size, total_dead, total_infected, saved_from_vac):
        infected_percentage = f"{float(total_infected / pop_size)}%"
        dead_percentage = f"{float(total_dead / pop_size)}%"

        with open(self.file_name, 'a') as f:
            f.write(f"Infected percentage: {infected_percentage} Dead_percentage: {dead_percentage} Interactions saved from vaccination: {saved_from_vac}")
