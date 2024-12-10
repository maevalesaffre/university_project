package vehicle.bike.bikeDecorator;

import static org.junit.Assert.*;
import org.junit.Test;

import observer.ControlCenter;
import vehicle.bike.Bike;

import org.junit.Before;

public class LuggageRackDecorTest {
    
    private ControlCenter controlCenter;
    private Bike bike;
    private LuggageRackDecor bikeWithLuggageRack;



    @Before
    public void setUp() {
        controlCenter = ControlCenter.getInstance();
        bike = new Bike(1, true, true, false, controlCenter);
        bikeWithLuggageRack = new LuggageRackDecor(bike, 15);
    }

    @Test
    public void testGetLuggageRackCapacity() {
        assertEquals(15, bikeWithLuggageRack.getLuggageRackCapacity());
    }

    @Test
    public void testIsLuggageRackDetached() {
        assertFalse(bikeWithLuggageRack.isLuggageRackDetached());
    }

    @Test
    public void testSetLuggageRackDetached() {
        bikeWithLuggageRack.setLuggageRackDetached(true);
        assertTrue(bikeWithLuggageRack.isLuggageRackDetached());
    }

}
