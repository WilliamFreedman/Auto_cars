public class Vector2 implements Comparable<Vector2> {
    private double x;
    private double y;

    public Vector2(double x, double y)
    {
        this.x = x;
        this.y = y;
    }

    public double getX()
    {
        return x;
    }

    public double getY()
    {
        return y;
    }

    public int compareTo(Vector2 other)
    {
        if (mag()>other.mag())
        {
            return 1;
        }
        if (mag()<other.mag())
        {
            return -1;
        }
        else
        {
            return 0;
        }
    }

    public int hashCode()
    {
        return Double.hashCode(x+y);
    }

    public boolean equals(Vector2 other)
    {
        return x == other.x && y == other.y;
    }


    public Vector2 add(Vector2 o)
    {
        return new Vector2(x+o.x,y+o.y);
    }

    public Vector2 mul(double scaling)
    {
        return new Vector2(x*scaling,y*scaling);
    }

    public double mag()
    {
        return Math.sqrt(Math.pow(x,2)+Math.pow(y,2));
    }

    public Vector2 update(double x, double y)
    {
        this.x = x;
        this.y = y;
        return this;
    }

    public Vector2 update(Vector2 v)
    {
        return update(v.x,v.y);
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
