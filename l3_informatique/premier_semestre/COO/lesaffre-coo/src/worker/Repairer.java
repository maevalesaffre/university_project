package worker;

import exceptions.StationCapacityExceededException;
import observer.Station;
import vehicle.bike.Bike;
import vehicle.bike.bikeDecorator.*;

/**
 * A class representing a repairer, which is a type of worker.
 */
public class Repairer implements Worker {

    /**
     * Perform repair work on a basic bike.
     *
     * @param bike The basic bike to perform repair work on.
     */
    @Override
    public void work(Bike bike) {

        System.out.println("Nothing to repair on the bicycle.\n");
        bike.setOffService(false);
    }

    /**
     * Perform repair work on a bike with a basket decoration.
     *
     * @param basketBicycleDecor The bike with a basket decoration to perform repair work on.
     */
    @Override
    public void work(BasketBicycleDecor basketBicycleDecor) {
        

        int cpt = 10;
        int currentcpt=0;
        
        System.out.println("Wait 10 sec for repairing the vehicle\n");

        while(currentcpt<cpt){ // we wait 10 turns before repair
            currentcpt ++;
        } 
    
        if (basketBicycleDecor.isBasketDetached()) {
            basketBicycleDecor.setBasketDetached(false);
            System.out.println("The bicycle basket has been repaired.");
        }
        basketBicycleDecor.setOffService(false);

    }

    /**
     * Perform repair work on a bike with a luggage rack decoration.
     *
     * @param luggageRackDecor The bike with a luggage rack decoration to perform repair work on.
     */
    @Override
    public void work(LuggageRackDecor luggageRackDecor) {
        int cpt = 10;
        int currentcpt=0;
        System.out.println("Wait 10 sec for repairing the vehicle\n");

        while(currentcpt<cpt){ // we wait 10 turns before repair
            currentcpt ++;
        } 
    
        
        if (luggageRackDecor.isLuggageRackDetached()) {
            luggageRackDecor.setLuggageRackDetached(false);
            System.out.println("The bicycle luggage rack has been repaired.");
        }

        luggageRackDecor.setOffService(false);

    }

    @Override
    public void putInStation(Station station) throws StationCapacityExceededException {
    }
}
