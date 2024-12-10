package exceptions;

/**
 * An exception to indicate that an operation on a station is not allowed because the station has reached its maximum capacity.
 */
public class StationCapacityExceededException extends Exception {

    /**
     * Constructs a new StationCapacityExceededException with a default error message.
     */
    public StationCapacityExceededException() {
        super("No more places available.");
    }
}
