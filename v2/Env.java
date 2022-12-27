import java.util.HashSet;
public class Env {

    private int height;
    private int width;

    private HashSet<Car> cars;

    public HashSet<Car> getCars()
    {
        return cars;
    }

    public boolean newCar(Car c)
    {
        return cars.add(c);
    }



}
