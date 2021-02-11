package main

import (
	"fmt"
	"net/http"
	"html/template"
)

type App struct {
	Title string
	Nutzer map[string]int
}

func nutzer_Handler(w http.ResponseWriter, r *http.Request) {
	app := App{"MyApp", map[string]int{"Ben":17, "Nick":13, "Luke":16}}

	t, _ := template.ParseFiles("p17_template.html")
	t.Execute(w, app)
}

func index_Handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello there")
	fmt.Fprintf(w, "General Kenobi!")
}

func main() {
	http.HandleFunc("/", index_Handler)
	http.HandleFunc("/nutzer/", nutzer_Handler)
	http.ListenAndServe(":3000", nil)

}