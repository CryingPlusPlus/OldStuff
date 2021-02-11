package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {
	resp, _ := http.Get("https://www.washingtonpost.com/news-sitemap-index.xml")
	bytes, _ := ioutil.ReadAll(resp.Body)
	stringBody := string(bytes)
	fmt.Println(stringBody)
	resp.Body.Close()
}	