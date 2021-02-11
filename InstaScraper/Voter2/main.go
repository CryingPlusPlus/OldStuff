package main

import (
	"fmt"
	"net/http"
	"html/template"
	"os"
	"bufio"
	"strings"
)

var pL pictureList
//Structs --------------------------------------------------------------------------------------------

type pictureList struct {
	Pics []string
	Info map[string]string
}

type templateInfo struct {
	Pic string
	Done float64
}

func (p *pictureList) loadPics() {
	dir, err := os.Open("public/pics/")
	if err != nil {
		fmt.Println("\n\n\n\nError: ", err, "\n\n\n\n")
		return
	}
	defer dir.Close()
	list, _ := dir.Readdirnames(0)
	p.Pics = list
}

func (p *pictureList) loadInfo() {
	lines := []string{}
	fh, err := os.Open("mensch.data")
	defer fh.Close()
	if err != nil {
		fmt.Println("\n\n\n\nError: ", err, "\n\n\n\n")
		return
	}
	scanner := bufio.NewScanner(fh)
	for scanner.Scan() {
              lines = append(lines, scanner.Text())
    }
    
    for _, line := range lines {
    	info := strings.Split(line, ":")
    	p.Info[info[0]] = info[1]
    }
}

func (p *pictureList) cutPics() {
	cIndex := 0
	for true {
		if cIndex == len(p.Pics) {
			break
		}
		_, known := p.Info[p.Pics[cIndex]]
		if known {
			p.Pics = remove(p.Pics, cIndex)
		} else {
			cIndex++
		}
	}
}

func (p *pictureList) init() {
	p.loadPics()
	p.loadInfo()
	p.cutPics()
}

func (p *pictureList) saveInfo() {
	output := ""

	for key, val := range p.Info {
		output += key + ":" + val + "\n"
	}

	fh, err := os.Create("mensch.data")
	defer fh.Close()
	if err != nil {
		fmt.Println(err)
		return
	}
	fh.WriteString(output)
	return 
}
//funcs -------------------------------------------------------------------------------------------

func remove(s []string, i int) []string {
    s[i] = s[len(s)-1]
    // We do not need to put s[i] at the end, as it will be discarded anyway
    return s[:len(s)-1]
}


//site handlers --------------------------------------------------------------------------------------

func save_Handler(w http.ResponseWriter, r *http.Request) {
	pL.saveInfo()
	http.Redirect(w, r, "/", http.StatusSeeOther)
}

func submit_Handler(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()
	if r.Method == "POST" {
		value := r.Form
		fmt.Println(value["PicButton"][0])
		pL.Info[pL.Pics[0]] = value["PicButton"][0]
		pL.Pics = remove(pL.Pics, 0)
	}

	http.Redirect(w, r, "/", http.StatusSeeOther)
}

func index_Handler(w http.ResponseWriter, r *http.Request) {
	tInfo := templateInfo{pL.Pics[0], float64(len(pL.Info))/float64(14192) * float64(100)}
	t, _ := template.ParseFiles("index_template.html")
	t.Execute(w, tInfo)
}
//main -----------------------------------------------------------------------------------------------
func main() {
	pL = pictureList{Info:map[string]string{}}
	pL.init()
	http.Handle("/public/", http.StripPrefix("/public/", http.FileServer(http.Dir("public"))))
	http.HandleFunc("/", index_Handler)
	http.HandleFunc("/submit/", submit_Handler)
	http.HandleFunc("/save/", save_Handler)
	http.ListenAndServe(":3000", nil)
}