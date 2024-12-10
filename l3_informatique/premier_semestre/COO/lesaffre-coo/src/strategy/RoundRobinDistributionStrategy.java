package strategy;
import java.util.List;
import exceptions.StationCapacityExceededException;
import observer.Station;
import vehicle.Vehicle;


public class RoundRobinDistributionStrategy implements StrategyDistribution {

    private int currentIndex = 0; // Keep track of the current target station index.
    
    /**
     * Redistribute vehicles from a source station to other stations.
     *
     * @param vehicles The list of vehicles to be redistributed.
     * @param stations The list of stations to which vehicles are redistributed.
     * @throws StationCapacityExceededException If the maximum station capacity is exceeded during redistribution.
     */
    @Override
    public void redistribute(List<Vehicle> vehicles, List<Station> stations) throws StationCapacityExceededException {
    
        for (Vehicle vehicle : vehicles) {
            if (vehicle.getState()) {
                currentIndex = (currentIndex + 1) % stations.size();

                Station station = stations.get(currentIndex);

                if (station.getVehicles().size() < station.getCapacity()) {
                    station.addVehicle(vehicle);
            }
                currentIndex = (currentIndex + 1) % stations.size();
            }
        }
    }
}
   