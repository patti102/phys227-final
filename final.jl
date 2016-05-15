a = 0.2
b = 0.2
c = 2
dt = 0.001
num = 500000
t = linspace(0, 500, num)
x_array = zeros(Float64, num)
y_array = zeros(Float64, num)
z_array = zeros(Float64, num)

function x_dot(t, x, y, z)
    (- y - z)
end

function y_dot(t, x, y, z)
    (x + a * y)
end

function z_dot(t, x, y, z)
    (b + z * (x - c))
end

function run()

    x = 0
    y = 0
    z = 0

    for i = 2:num
        k1_x = dt*x_dot(t[i-1], x, y, z)
        k1_y = dt*y_dot(t[i-1], x, y, z)
        k1_z = dt*z_dot(t[i-1], x, y, z)

        k2_x = dt*x_dot(t[i-1] + dt / 2.0, x + 0.5*k1_x, y + 0.5*k1_y, z + 0.5*k1_z)
        k2_y = dt*y_dot(t[i-1] + dt / 2.0, x + 0.5*k1_x, y + 0.5*k1_y, z + 0.5*k1_z)
        k2_z = dt*z_dot(t[i-1] + dt / 2.0, x + 0.5*k1_x, y + 0.5*k1_y, z + 0.5*k1_z)

        k3_x = dt*x_dot(t[i-1] + dt / 2.0, x + 0.5*k2_x, y + 0.5*k2_y, z + 0.5*k2_z)
        k3_y = dt*y_dot(t[i-1] + dt / 2.0, x + 0.5*k2_x, y + 0.5*k2_y, z + 0.5*k2_z)
        k3_z = dt*z_dot(t[i-1] + dt / 2.0, x + 0.5*k2_x, y + 0.5*k2_y, z + 0.5*k2_z)

        k4_x = dt*x_dot(t[i-1] + dt / 2.0, x + k3_x, y + k3_y, z + k3_z)
        k4_y = dt*y_dot(t[i-1] + dt / 2.0, x + k3_x, y + k3_y, z + k3_z)
        k4_z = dt*z_dot(t[i-1] + dt / 2.0, x + k3_x, y + k3_y, z + k3_z)
        
        x_array[i] = x + (k1_x + k2_x + k2_x + k3_x + k3_x + k4_x)/6
        y_array[i] = y + (k1_y + k2_y + k2_y + k3_y + k3_y + k4_y)/6
        z_array[i] = z + (k1_z + k2_z + k2_z + k3_z + k3_z + k4_z)/6

        x = x + (k1_x + k2_x + k2_x + k3_x + k3_x + k4_x)/6
        y = y + (k1_y + k2_y + k2_y + k3_y + k3_y + k4_y)/6
        z = z + (k1_z + k2_z + k2_z + k3_z + k3_z + k4_z)/6

    end
    x_array, y_array, z_array
end

@time run()