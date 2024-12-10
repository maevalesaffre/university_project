package exceptions;

/**
 * An exception to indicate that an operation on a station is not allowed because the station is empty.
 */
public class StationEmptyException extends Exception {

    /**
     * Constructs a new StationEmptyException with a default error message.
     */
    public StationEmptyException() {
        super("Station empty.");
    }
}
