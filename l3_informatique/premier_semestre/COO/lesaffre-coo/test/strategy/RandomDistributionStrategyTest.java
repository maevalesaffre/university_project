package strategy;

import static org.junit.Assert.*;
import org.junit.Test;

import exceptions.StationCapacityExceededException;
import observer.ControlCenter;
import observer.Station;
import vehicle.Vehicle;
import vehicle.bike.Bike;

import org.junit.Before;

import java.util.ArrayList;
import java.util.List;

public class RandomDistributionStrategyTest {

    private RandomDistributionStrategy distributionStrategy;
    private List<Vehicle> vehicles;
    private List<Station> stations;
    private ControlCenter controlCenter;

    @Before
    public void setUp() {
        distributionStrategy = new RandomDistributionStrategy();
        vehicles = new ArrayList<>();
        stations = new ArrayList<>();
        controlCenter = ControlCenter.getInstance();
    }

    @Test
    public void testRedistribute() throws StationCapacityExceededException {
        Vehicle vehicle1 = new Bike(1, true, true, false, controlCenter);
        Vehicle vehicle2 = new Bike(2, true, true, false, controlCenter);
        Vehicle vehicle3 = new Bike(3, true, true, false, controlCenter);

        vehicles.add(vehicle1);
        vehicles.add(vehicle2);
        vehicles.add(vehicle3);

        Station station1 = new Station(1,"station 1 ");
        Station station2 = new Station(2 , "station 2 ");

        stations.add(station1);
        stations.add(station2);

        distributionStrategy.redistribute(vehicles, stations);

        assertTrue(station1.getVehicles().size() <= station1.getCapacity());
        assertTrue(station2.getVehicles().size() <= station2.getCapacity());
    }
}
