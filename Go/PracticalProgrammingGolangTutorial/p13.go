package main

import (
	"fmt"
	"net/http"
	"html/template"
)

type NewsAggPage struct {
	Title string
	News string
}

func newsAgg_Handler(w http.ResponseWriter, r *http.Request) {
	p := NewsAggPage{
		Title: "The Title",
		News: "The News",
	}

	t, _ := template.ParseFiles("basictemplating.html")
	t.Execute(w, p)
}

func index_Handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello There")
}

func main() {
	http.HandleFunc("/", index_Handler)
	http.HandleFunc("/agg/", newsAgg_Handler)
	http.ListenAndServe(":3000", nil)

}