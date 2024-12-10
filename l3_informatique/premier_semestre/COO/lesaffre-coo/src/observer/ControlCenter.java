package observer;

import java.util.ArrayList;
import java.util.List;

import exceptions.StationCapacityExceededException;
import strategy.*;
import vehicle.*; 
import worker.*;

/**
 * The ControlCenter class represents the central control unit in a vehicle management system.
 * It implements the Observer interface to receive updates about the state of vehicles.
 * This class follows the Singleton pattern to ensure a single instance.
 */
public class ControlCenter implements Observer {

    private static ControlCenter instance;
    private List<Vehicle> vehicles;
    private StrategyDistribution strategy;
    private List<Station> stations;


    private long interval;

    /**
     * Private constructor to initialize the ControlCenter with empty lists for vehicles and stations.
     */
    private ControlCenter() {
        vehicles = new ArrayList<>();
        this.stations = new ArrayList<>();
    }

    /**
     * Gets the singleton instance of ControlCenter. If an instance does not exist, a new one is created.
     *
     * @return The ControlCenter instance.
     */
    public static ControlCenter getInstance() {
        if (instance == null) {
            instance = new ControlCenter();
        }
        return instance;
    }

    /**
     * Adds a vehicle to the list of managed vehicles.
     *
     * @param vehicle The vehicle to be added.
     */
    @Override
    public void addVehicle(Vehicle vehicle) {
        vehicles.add(vehicle);
    }

    /**
     * Updates the ControlCenter based on the state of the provided vehicle.
     *
     * @param vehicle The vehicle that triggered the update.
     */
    @Override
    public void update(Vehicle vehicle) {
        if (vehicle.getOffService()) {
            System.out.println("The vehicle " + vehicle.getId() + " is out of service. A repairman was sent.");
            Repairer repairer = new Repairer();
            vehicle.accept(repairer);
        } else if (vehicle.getState()) {
            System.out.println("The vehicle " + vehicle.getId() + " is in service.");
        } else if (!vehicle.getState()) {
            System.out.println("The vehicle " + vehicle.getCondition() + " has been stolen.");
            vehicles.remove(vehicle);
        }
    }

    /**
     * Sets the redistribution strategy for managing the distribution of vehicles.
     *
     * @param strategy The redistribution strategy to be set.
     */
    public void setStrategy(StrategyDistribution strategy) {
        this.strategy = strategy;
    }

    /**
     * Adds a station to the list of managed stations.
     *
     * @param station The station to be added.
     */
    public void addStation(Station station) {
        stations.add(station);
    }

    /**
     * Redistributes vehicles among stations based on the defined strategy.
     * Prints a message if no redistribution strategy is defined.
     * @throws StationCapacityExceededException
     */
    public void redistribute() throws StationCapacityExceededException {
        
        if (this.strategy != null) {

            this.strategy.redistribute(vehicles, stations);

        } else {
            System.out.println("No redistribution strategy has been defined.");
        }
    }

    /**
     * get the list of vehicles
     * @return list of vehicles
     */
    public List<Vehicle> getVehicles() {
        return this.vehicles;
    }


    /**
     * update the information of the behavior change from the station;
	 * If one of them is empty, we make a redistribution of the vehicle in all station
	 * If one of them is full, we make a redistribution of the vehicle in all station
	 * else do nothing
	 */
	public void update() {
		boolean notifyRedistribution = false;
	    for (Station station : this.stations){

	    	notifyRedistribution = station.notifyControlCenter();
            if (notifyRedistribution) {
                try{
                    System.out.println("======================================================================\n");
                    
                    System.out.println("                     REDISTRIBUTION                      ");

                    System.out.println("======================================================================\n");

                    this.redistribute();

                    System.out.println("======================================================================\n");

                    
                    System.out.println("                 END OF THE  REDISTRIBUTION               ");

                    System.out.println("======================================================================\n");

                    break;
                }
                catch(StationCapacityExceededException e){
                    System.out.println("Error during redistribution of stations : A station is full");
                }
            }
        
        }
        
        System.out.println("======================================================================\n");
        
        System.out.println(" CHECK IF SOME VEHICLES SHOULD TO BECOME OUT OF SERVICE ");
        
        System.out.println("======================================================================\n");
        
        Boolean somthingTorepair = false;
	    
        for(Vehicle vehicle : vehicles){
            if(vehicle.getNbLocations() >= vehicle.getMaxNbLocations()){
                vehicle.setOffService(true);

                somthingTorepair = true;
            }
        }

        if(!somthingTorepair){
            System.out.println(" No vehicle to repair \n");
        }


        System.out.println("======================================================================\n");
        
        System.out.println("                 CHECK IF SOME VEHICLES ARE STOLEN                      ");
        
        System.out.println("======================================================================\n");
      
        for (Station station : stations){
            station.checkVehicles();
        }

	     System.out.println("======================================================================\n");
        
        System.out.println("               END OF CHECKING THE STATE OF VEHICLES                     ");
        
        
        System.out.println("======================================================================\n");



	}

	/**
     * get the interval
     * @return the interval
     */
	public long getInterval() {
		return this.interval;
	}

public void setInterval(long interval) {
        this.interval = interval;
    }





}
