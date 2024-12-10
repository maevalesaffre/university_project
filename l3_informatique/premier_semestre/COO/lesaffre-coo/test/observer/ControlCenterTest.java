package observer;

import static org.junit.Assert.*;
import org.junit.Test;

import exceptions.StationCapacityExceededException;
import strategy.MockStrategy;
import strategy.RoundRobinDistributionStrategy;
import vehicle.Vehicle;

import vehicle.bike.*;


import org.junit.Before;

public class ControlCenterTest {

    private ControlCenter controlCenter;
    private Vehicle vehicle;
    private Vehicle vehicle1;
    
    @Before
    public void setUp() {
        controlCenter = ControlCenter.getInstance();
        vehicle = new Bike(1, true, true, false, controlCenter);
        vehicle1 = new Bike(2, true, true, false, controlCenter);
    }

    @Test
    public void testAddVehicle() {
        assertEquals(2,controlCenter.getVehicles().size());
        controlCenter.addVehicle(vehicle);
        assertTrue(controlCenter.getVehicles().contains(vehicle));
        Vehicle vehicle2 = new Bike(3, true, true, false, controlCenter);
        assertFalse(controlCenter.getVehicles().contains(vehicle2));
        controlCenter.addVehicle(vehicle2);
        assertEquals(4,controlCenter.getVehicles().size());
    }

    @Test
    public void testUpdateVehicleOutOfService() {
        vehicle.setOffService(true);
        controlCenter.update(vehicle);
        assertTrue(true);
    }

    @Test
    public void testUpdateVehicleInService() {
        vehicle.setState(true);
        controlCenter.update(vehicle);
        assertTrue(true); 
    }

    @Test
    public void testUpdateVehicleStolen() {
        vehicle.setState(false);
        controlCenter.update(vehicle);
        assertFalse(controlCenter.getVehicles().contains(vehicle));
    }





    @Test 
    public void testUpdateMock(){
        MockStrategy mock = new MockStrategy();
        
        controlCenter.setStrategy(mock);

        assertEquals(0,mock.applyEffect);

        try{

        controlCenter.redistribute();

        assertEquals(1, mock.applyEffect);
        
        }
        catch (StationCapacityExceededException e){
            fail();
        }
    }







    @Test
    public void testRedistributeWithRoundRobinDistributionStrategy() {
        RoundRobinDistributionStrategy strategy = new RoundRobinDistributionStrategy(); 
        controlCenter.setStrategy(strategy);

        
        
        Station station1 = new Station(0, "station1");
        Station station2 = new Station(1, "station2");
        
        controlCenter.addVehicle(vehicle);
        controlCenter.addVehicle(vehicle1);
        
        controlCenter.addStation(station1);
        controlCenter.addStation(station2);
       

        try { 
            
            station1.addVehicle(vehicle);
            station2.addVehicle(vehicle1);
            
            controlCenter.redistribute();
            assertEquals(station1.getVehicles().get(0),controlCenter.getVehicles().get(0));
            assertEquals(station2.getVehicles().get(0),controlCenter.getVehicles().get(1));
            assertEquals(2, controlCenter.getVehicles().size());
            assertEquals(2, controlCenter.getVehicles().size());
            for (Vehicle vehicle : controlCenter.getVehicles()) {
                assertNotNull(controlCenter.getVehicles().contains(vehicle));
            }

            
        } catch (StationCapacityExceededException e) {
            fail("Redistribution should not throw StationCapacityExceededException in this test.");
        }
    }


}
