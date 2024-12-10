package vehicle.bike.bikeDecorator;

import static org.junit.Assert.*;
import org.junit.Test;

import observer.ControlCenter;
import vehicle.bike.Bike;

import org.junit.Before;

public class BasketBicycleDecorTest {
    
    private ControlCenter controlCenter;
    private Bike bike;
    private BasketBicycleDecor bikeWithBasket;

    @Before
    public void setUp() {
        controlCenter = ControlCenter.getInstance();
        bike = new Bike(1, true, true, false, controlCenter);
        bikeWithBasket = new BasketBicycleDecor(bike, 10);
    }

    @Test
    public void testGetBasketCapacity() {
        assertEquals(10, bikeWithBasket.getBasketCapacity());
    }

    @Test
    public void testIsBasketDetached() {
        assertFalse(bikeWithBasket.isBasketDetached());
    }

    @Test
    public void testSetBasketDetached() {
        bikeWithBasket.setBasketDetached(true);
        assertTrue(bikeWithBasket.isBasketDetached());
    }

}
