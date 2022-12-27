public class Car {

    private Vector2 position;
    private Vector2 velocity;
    private Vector2 acceleration;

    public Vector2 updatePosition(int x, int y)
    {
        position.update(x,y);
        return position;
    }

    public Vector2 updateVelocity(int x, int y)
    {
        velocity.update(x,y);
        return velocity;
    }

    public Vector2 updateAcceleration(int x, int y)
    {
        acceleration.update(x,y);
        return acceleration;
    }



}
