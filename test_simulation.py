from simulation import Simulation
from virus import Virus
from person import Person
from logger import Logger

def test_constructor():
    virus = Virus("HIV", 0.24, 0.12)
    sim = Simulation(10, .4, virus, 2)

    assert sim.pop_size == 10
    assert sim.virus == virus
    assert sim.initial_infected == 2
    assert sim.vacc_percentage == .4
    assert sim.next_person_id == 11
    assert sim.total_infected == 0
    assert sim.current_infected == 0
    assert sim.total_infected == 0
    assert sim.newly_infected == []
    assert sim.save_from_vac == 0
    assert sim.file_name == "_virus_name_HIV_simulation_pop_10_vp_0.4_infected_2.txt"

def test_simulation_should_continue():
    virus = Virus("HIV", 0.24, 0.12)
    sim = Simulation(10, .4, virus, 2)

    assert sim._simulation_should_continue()

def test_infect_newly():
    virus = Virus("HIV", 0.24, 0.12)
    sim = Simulation(10, .4, virus, 2)


    sim._infect_newly_infected()
    assert sim.total_infected == 0


def test_create_population():
    virus = Virus("HIV", 0.50, 0.50)
    sim = Simulation(10, .50, virus, 2)

    vaccination_count = 0
    infection_count = 0

    for person in sim.population:
        assert person.is_alive == True

        if person.is_vaccinated:
            vaccination_count += 1
        if person.infection is not None:
            infection_count += 1

    assert vaccination_count == 5
    assert infection_count == 2
    assert len(sim.population) == 10