package main

import (
	"fmt"
	"net/http"
)

func index_handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "<h1>Header1</h1>")
	fmt.Fprintf(w, "<p>paragraph</p>")
	fmt.Fprintf(w, "<h1>AnotherHEader</h1>")
}

func main() {
	http.HandleFunc("/", index_handler)
	http.ListenAndServe(":3000", nil)
}