FROM r-base:4.1.3

RUN Rscript -e 'install.packages("renv")'

WORKDIR /usr/local/src
COPY renv.lock .

RUN Rscript -e 'renv::restore()'

COPY . .

CMD ["Rscript", "main.R"]
