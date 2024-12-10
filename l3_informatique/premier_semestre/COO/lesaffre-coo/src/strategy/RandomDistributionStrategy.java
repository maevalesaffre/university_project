package strategy;
import java.util.List;
import java.util.Random;
import vehicle.Vehicle;
import observer.*;
import exceptions.StationCapacityExceededException;

    public class RandomDistributionStrategy implements StrategyDistribution {

    /**
     * Redistribute vehicles from a source station to other stations.
     *
     * @param vehicles The list of vehicles to be redistributed.
     * @param stations The list of stations to which vehicles are redistributed.
     * @throws StationCapacityExceededException If the maximum station capacity is exceeded during redistribution.
     */
        @Override
        public void redistribute(List<Vehicle> vehicles, List<Station> stations) throws StationCapacityExceededException {
            Random random = new Random();
            for (Vehicle vehicle : vehicles) {
                if (vehicle.getState()) {
                    int index = random.nextInt(stations.size());
                    Station station = stations.get(index);
                    if (station.getVehicles().size() < station.getCapacity()) {
                        System.out.println("Station : "+station.getName());
                        station.addVehicle(vehicle);
                    }
                }
            }
        }
}
   