package main

import (
	"fmt"
)

type car struct {
	gas_pedal uint16
	brake uint16
	steering_wheel int16
	top_speed_kmh float64
}

func (c *car) kmh() float64 {
	return c.gas_pedal
} 

func main() {
	a_car := car{22341, 0, 12561, 225.0}

}