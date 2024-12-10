package worker;

import org.junit.Test;

import observer.ControlCenter;
import vehicle.bike.Bike;
import vehicle.bike.bikeDecorator.BasketBicycleDecor;
import vehicle.bike.bikeDecorator.LuggageRackDecor;

import static org.junit.Assert.*;

public class RepairerTest {


	private ControlCenter controlCenter;

    @Test
    public void testWorkOnBasketBicycleDecor() {
    	controlCenter = ControlCenter.getInstance();
        Worker worker = new Repairer();
        Bike bike = new Bike(1, true, true, false, controlCenter); 
        BasketBicycleDecor basketBike = new BasketBicycleDecor(bike, 10); 
        worker.work(basketBike);
        assertFalse(basketBike.isBasketDetached()); 
    }

    @Test
    public void testWorkOnLuggageRackDecor() {
    	controlCenter = ControlCenter.getInstance();
        Worker worker = new Repairer();
        Bike bike = new Bike(1, true, true, false, controlCenter); 
        LuggageRackDecor luggageRackBike = new LuggageRackDecor(bike, 5); 
        worker.work(luggageRackBike);
        assertFalse(luggageRackBike.isLuggageRackDetached());
    }
    
}

