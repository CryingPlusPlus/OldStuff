package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
)

func renderTemplate(w http.ResponseWriter, r *http.Request) {
	parsedTemplate, _ := template.ParseFiles("Template/index.html")
	err := parsedTemplate.Execute(w, nil)
	if err != nil {
		log.Println("Error executing template :", err)
		return
	}
}

func login(w http.ResponseWriter, r *http.Request) {
	err := r.ParseForm()
	if err != nil {
		log.Fatal(err)
	}
	if r.Method == "POST" {
		for key, value := range r.Form {
			fmt.Println()
		}
	}
}

func main() {
	http.HandleFunc("/", renderTemplate)
	http.HandleFunc("/login", login)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatal("Error Starting the HTTP Server : ", err)
		return
	}
}