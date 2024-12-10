package observer;

import static org.junit.Assert.*;
import org.junit.Test;
import org.junit.Before;

import exceptions.StationCapacityExceededException;
import exceptions.StationEmptyException;
import vehicle.Vehicle;
import vehicle.bike.*;
import worker.Repairer;

public class StationTest {

    private ControlCenter controlCenter;

    private Station station;
    private Bike bike1;
    private Bike bike2;
    private Bike bike3;
    private Repairer repairer;

    @Before
    public void setUp() {

        controlCenter = ControlCenter.getInstance();
      
        station = new Station(1, "Station A");
        bike1 = new Bike(1, true, true, false, controlCenter);
        bike2 = new Bike(2, true, true, false, controlCenter);
        bike3 = new Bike(3, true, true, false, controlCenter);
        repairer = new Repairer();
        controlCenter.addStation(station);
        
    }

    @Test
    public void testGetIdStation() {
        assertEquals(1, station.getIdStation());
    }

    @Test
    public void testGetName() {
        assertEquals("Station A", station.getName());
    }

    @Test
    public void testGetCapacity() {
        assertTrue(10 <= station.getCapacity() && station.getCapacity()<=20);
    }

    @Test
    public void testAddVehicle() {
        try{
            station.addVehicle(bike1);
        }
        catch(StationCapacityExceededException e){
            fail();
        }
        assertTrue(station.getVehicles().contains(bike1));
        assertTrue(bike1.getState());
        assertEquals(station.getCapacity()-1, station.nbPlacesAvailables());
    }

    @Test(expected = StationCapacityExceededException.class)
    public void testAddVehicleExceedCapacity() throws StationCapacityExceededException {
        for (int i = 0; i < station.getCapacity()*10; i++) {
            station.addVehicle(new Bike(i, true, true, false, controlCenter));
        }
    }

    @Test
    public void testRemoveVehicle() throws StationCapacityExceededException, StationEmptyException {
        station.addVehicle(bike1);
        station.removeVehicle(bike1);
        assertFalse(station.getVehicles().contains(bike1));
        assertFalse(bike1.getState());
        assertEquals(station.getCapacity(), station.nbPlacesAvailables());
    }

    @Test(expected = StationEmptyException.class)
    public void testRemoveVehicleFromEmptyStation() throws StationEmptyException {
        station.removeVehicle(bike1);
    }

    @Test
    public void testIsEmpty() {
        assertTrue(station.isEmpty());
        try{
            station.addVehicle(bike1);
        }
        catch(StationCapacityExceededException e){
            fail();
        }
        assertFalse(station.isEmpty());
    }

    @Test
    public void testNbPlacesAvailables() throws StationCapacityExceededException {
        assertEquals(station.getCapacity(), station.nbPlacesAvailables());
        station.addVehicle(bike1);
        assertEquals(station.getCapacity()-1, station.nbPlacesAvailables());
        station.addVehicle(bike2);
        assertEquals(station.getCapacity()-2, station.nbPlacesAvailables());
    }

    @Test
    public void testAddAndRemoveMultipleVehicles() throws StationCapacityExceededException, StationEmptyException {
        station.addVehicle(bike1);
        station.addVehicle(bike2);
        station.addVehicle(bike3);

        assertTrue(station.getVehicles().contains(bike1));
        assertTrue(station.getVehicles().contains(bike2));
        assertTrue(station.getVehicles().contains(bike3));

        assertEquals(station.getCapacity()-3, station.nbPlacesAvailables());

        station.removeVehicle(bike1);
        assertFalse(station.getVehicles().contains(bike1));
        assertTrue(station.getVehicles().contains(bike2));
        assertTrue(station.getVehicles().contains(bike3));

        assertEquals(station.getCapacity()-2, station.nbPlacesAvailables());

        station.removeVehicle(bike2);
        assertFalse(station.getVehicles().contains(bike1));
        assertFalse(station.getVehicles().contains(bike2));
        assertTrue(station.getVehicles().contains(bike3));

        assertEquals(station.getCapacity()-1, station.nbPlacesAvailables());

        station.removeVehicle(bike3);
        assertFalse(station.getVehicles().contains(bike1));
        assertFalse(station.getVehicles().contains(bike2));
        assertFalse(station.getVehicles().contains(bike3));

        assertEquals(station.getCapacity(), station.nbPlacesAvailables());
    }


    @Test
    public void testTakeVehicleFromEmptyStation() {
        Vehicle takenVehicle = station.takeVehicle(repairer);
        assertNull(takenVehicle);
        assertTrue(station.getVehicles().isEmpty());
    }


    @Test
    public void testTakeVehicleFromNonEmptyStation() throws StationEmptyException {
        Vehicle vehicle = new Bike(4, true, true, false, controlCenter);
        try {
            station.addVehicle(vehicle);
            Vehicle takenVehicle = station.takeVehicle(repairer);
            assertNotNull(takenVehicle);
            assertTrue(takenVehicle.getState()); 
            assertTrue(station.getVehicles().isEmpty()); 
        } catch (StationCapacityExceededException e) {
            e.printStackTrace();
            fail("Exception should not have been thrown");
        }

    }

    @Test
    public void testCheckVehiclesNoConditionSet() throws StationCapacityExceededException {

        Vehicle vehicle = new Bike(5, true, false, false, controlCenter);
        try {
            station.addVehicle(vehicle);
            station.checkVehicles();
            assertTrue(vehicle.getCondition());
        } catch (StationCapacityExceededException e) {
            e.printStackTrace();
            fail("Exception should not have been thrown");
        }

    }

    @Test
    public void testCheckVehiclesConditionSetAfterTwoTurns() throws StationCapacityExceededException {
        Vehicle vehicle = new Bike(6, true, false, false, controlCenter);
        station.addVehicle(vehicle);

        controlCenter.update();
        controlCenter.update();

        station.checkVehicles();

        assertTrue(vehicle.getCondition());
    }


    @Test
    public void testCheckVehiclesConditionNotSetBeforeTwoTurns() throws StationCapacityExceededException {
        Vehicle vehicle = new Bike(7, true, false, false, controlCenter);
        station.addVehicle(vehicle);

        controlCenter.update();


        station.checkVehicles();

        assertTrue(vehicle.getCondition());
    }
}

