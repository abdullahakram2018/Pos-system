function generatePDF(){
    const element = document.getElementById('pdf1');
  
    html2pdf()
    .from(element)
    .save();
  }