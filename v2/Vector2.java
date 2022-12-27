public class Vector2 {
    private double x;
    private double y;

    public Vector2(double x, double y)
    {
        this.x = x;
        this.y = y;
    }
    public Vector2 add(Vector2 o)
    {
        return new Vector2(x+o.x,y+o.y);
    }

    public Vector2 mul(float scaling)
    {
        return new Vector2(x*scaling,y*scaling);
    }

    public Vector2 update(int x, int y)
    {
        this.x = x;
        this.y = y;
        return this;
    }

    public double x()
    {
        return x;
    }
    public double y()
    {
        return y;
    }
}