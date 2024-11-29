
# Услвоие задачи
## Дано:
$$
r( \varphi ) = R \left( \sin ^2 \left( \frac{\varphi}{2} \right) - 4 \cos \varphi \right) = \frac{R}{2} \left( 1 - 9 \cos \varphi \right)
$$
$$
\varphi(t) = kt^2 - \omega t
$$
$$
R = 1 \ \text{м}, \quad k = 1 \ \frac{\text{рад}}{\text{c}^2}, \quad \omega = 1 \ \frac{\text{рад}}{\text{c}}, \quad t_0 = 1 \ \text{с}
$$

## Найти:
1. Скорости
$$
v(t), \ \dot{\varphi}(t)
$$

2. Ускорения
$$
w_\tau(t), \ w_n(t)
$$

3. Радиус кривизны
$$
\rho(t), \ \rho(t_0)
$$

4. Выполнить проверку
$$
\rho(t) \ \rightarrow \ \rho(t_0)
$$


# 1. Скорости
$$
x = r \cos(\varphi) = - \frac{9 \cos^{2}{\left(t^{2} - t \right)}}{2} + \frac{\cos{\left(t^{2} - t \right)}}{2}
$$

$$
y = r \sin(\varphi) = - \frac{9 \sin{\left(t^{2} - t \right)} \cos{\left(t^{2} - t \right)}}{2} + \frac{\sin{\left(t^{2} - t \right)}}{2}
$$

$$
v_x = \dot{x} = \left(t - \frac{1}{2}\right) \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \sin{\left(t \left(t - 1\right) \right)}
$$

$$
v_y = \dot{y} = \frac{\left(9 - 18 t\right) \cos^{2}{\left(t \left(t - 1\right) \right)}}{2} + \frac{\left(2 t - 1\right) \cos{\left(t \left(t - 1\right) \right)}}{2} + \frac{\left(18 t - 9\right) \sin^{2}{\left(t \left(t - 1\right) \right)}}{2}
$$

$$
v = \sqrt{v_x^2 + v_y^2}, \quad \dot{\varphi} = \frac{d \varphi}{dt}
$$

$$
v(t) = \frac{\sqrt{\left(2 t - 1\right)^{2} \left(\left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)^{2} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)}\right)}}{2}
$$

$$
\dot{\varphi}(t) = 2 t - 1
$$

# 2. Ускорения
$$
w_x = \dot{v_x} = \frac{\left(2 t - 1\right)^{2} \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \cos{\left(t \left(t - 1\right) \right)}}{2} - 9 \left(2 t - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \sin{\left(t \left(t - 1\right) \right)}
$$

$$
w_y = \dot{v_y} = - \frac{\left(2 t - 1\right)^{2} \sin{\left(t \left(t - 1\right) \right)}}{2} + 9 \left(2 t - 1\right)^{2} \sin{\left(2 t \left(t - 1\right) \right)} + 9 \sin^{2}{\left(t \left(t - 1\right) \right)} - 9 \cos^{2}{\left(t \left(t - 1\right) \right)} + \cos{\left(t \left(t - 1\right) \right)}
$$

$$
w = \sqrt{w_x^2 + w_y^2} = \sqrt{\left(\frac{\left(2 t - 1\right)^{2} \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \cos{\left(t \left(t - 1\right) \right)}}{2} - 9 \left(2 t - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \sin{\left(t \left(t - 1\right) \right)}\right)^{2} + \left(- \frac{\left(2 t - 1\right)^{2} \sin{\left(t \left(t - 1\right) \right)}}{2} + 9 \left(2 t - 1\right)^{2} \sin{\left(2 t \left(t - 1\right) \right)} + 9 \sin^{2}{\left(t \left(t - 1\right) \right)} - 9 \cos^{2}{\left(t \left(t - 1\right) \right)} + \cos{\left(t \left(t - 1\right) \right)}\right)^{2}}
$$

$$
w_\tau = \frac{dv}{dt} = \frac{\sqrt{\left(2 t - 1\right)^{2} \left(\left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)^{2} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)}\right)} \left(\frac{\left(2 t - 1\right)^{2} \left(2 \left(2 t - 1\right) \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin{\left(t \left(t - 1\right) \right)} \cos{\left(t \left(t - 1\right) \right)} - 36 \left(2 t - 1\right) \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \sin^{3}{\left(t \left(t - 1\right) \right)} + \left(- 2 \left(2 t - 1\right) \sin{\left(t \left(t - 1\right) \right)} + 18 \left(4 t - 2\right) \sin{\left(2 t \left(t - 1\right) \right)}\right) \left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)\right)}{2} + \frac{\left(8 t - 4\right) \left(\left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)^{2} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)}\right)}{2}\right)}{2 \left(2 t - 1\right)^{2} \left(\left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)^{2} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)}\right)}
$$

$$
w_n = \sqrt{w^2 - w_\tau^2} =  \sqrt{\left(\frac{\left(2 t - 1\right)^{2} \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \cos{\left(t \left(t - 1\right) \right)}}{2} - 9 \left(2 t - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \sin{\left(t \left(t - 1\right) \right)}\right)^{2} + \left(- \frac{\left(2 t - 1\right)^{2} \sin{\left(t \left(t - 1\right) \right)}}{2} + 9 \left(2 t - 1\right)^{2} \sin{\left(2 t \left(t - 1\right) \right)} + 9 \sin^{2}{\left(t \left(t - 1\right) \right)} - 9 \cos^{2}{\left(t \left(t - 1\right) \right)} + \cos{\left(t \left(t - 1\right) \right)}\right)^{2} - \frac{\left(\frac{\left(2 t - 1\right)^{2} \left(2 \left(2 t - 1\right) \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin{\left(t \left(t - 1\right) \right)} \cos{\left(t \left(t - 1\right) \right)} - 36 \left(2 t - 1\right) \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \sin^{3}{\left(t \left(t - 1\right) \right)} + \left(- 2 \left(2 t - 1\right) \sin{\left(t \left(t - 1\right) \right)} + 18 \left(4 t - 2\right) \sin{\left(2 t \left(t - 1\right) \right)}\right) \left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)\right)}{2} + \frac{\left(8 t - 4\right) \left(\left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)^{2} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)}\right)}{2}\right)^{2}}{4 \left(2 t - 1\right)^{2} \left(\left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)^{2} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)}\right)}}
$$

# 3. Радиус кривизны
$$
w_n = \frac{v^2}{\rho} \ \Rightarrow \ \rho = \frac{v^2}{w_n}
$$

$$
\rho = \frac{\left(2 t - 1\right)^{2} \left(\left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)^{2} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)}\right)}{4 \sqrt{\left(\frac{\left(2 t - 1\right)^{2} \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \cos{\left(t \left(t - 1\right) \right)}}{2} - 9 \left(2 t - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \sin{\left(t \left(t - 1\right) \right)}\right)^{2} + \left(- \frac{\left(2 t - 1\right)^{2} \sin{\left(t \left(t - 1\right) \right)}}{2} + 9 \left(2 t - 1\right)^{2} \sin{\left(2 t \left(t - 1\right) \right)} + 9 \sin^{2}{\left(t \left(t - 1\right) \right)} - 9 \cos^{2}{\left(t \left(t - 1\right) \right)} + \cos{\left(t \left(t - 1\right) \right)}\right)^{2} - \frac{\left(\frac{\left(2 t - 1\right)^{2} \left(2 \left(2 t - 1\right) \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin{\left(t \left(t - 1\right) \right)} \cos{\left(t \left(t - 1\right) \right)} - 36 \left(2 t - 1\right) \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right) \sin^{3}{\left(t \left(t - 1\right) \right)} + \left(- 2 \left(2 t - 1\right) \sin{\left(t \left(t - 1\right) \right)} + 18 \left(4 t - 2\right) \sin{\left(2 t \left(t - 1\right) \right)}\right) \left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)\right)}{2} + \frac{\left(8 t - 4\right) \left(\left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)^{2} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)}\right)}{2}\right)^{2}}{4 \left(2 t - 1\right)^{2} \left(\left(\cos{\left(t \left(t - 1\right) \right)} - 9 \cos{\left(2 t \left(t - 1\right) \right)}\right)^{2} + \left(18 \cos{\left(t \left(t - 1\right) \right)} - 1\right)^{2} \sin^{2}{\left(t \left(t - 1\right) \right)}\right)}}}
$$

$$
\rho (t_0) = \frac{32}{17}
$$

# 4. Проверка радиуса кривизны
Рассчитаем радиус кривизны другим способом:

$$
\rho(\varphi) = \frac{ \left( r^2 + r'_\varphi \right)^{\frac{3}{2}} }{ \left| r^2 + 2{(r'_\varphi)}^2 - r r''_\varphi \right| }
$$

$$
r'_\varphi = \frac{9 \sin{\left(\varphi \right)}}{2}
$$

$$
r''_\varphi = \frac{9 \cos{\left(\varphi \right)}}{2}
$$

$$
\rho(\varphi) = \frac{\left(82 - 18 \cos{\left(\varphi \right)}\right)^{\frac{3}{2}}}{2 \left|{27 \cos{\left(\varphi \right)} - 163}\right|}
$$

$$
\rho(t) = \frac{\sqrt{2} \left(41 - 9 \cos{\left(t \left(t - 1\right) \right)}\right)^{\frac{3}{2}}}{\left|{27 \cos{\left(t \left(t - 1\right) \right)} - 163}\right|}
$$

$$
\rho(t_0) = \frac{32}{17}
$$

Проверка верна!

